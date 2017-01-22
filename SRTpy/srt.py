import os, re
from datetime import datetime
from xml.etree import ElementTree as ET

from error import *
from train import *
from utils import *
from reservation import *
from constants import TRAIN_CODE

SRT_HOST = 'https://app.srail.co.kr'
SRT_LOGIN = '{}/apb/selectListApb01080.do'.format(SRT_HOST)
SRT_LOGOUT = '{}/apb/selectListApb01081.do'.format(SRT_HOST)
SRT_SEARCH = '{}/ara/selectListAra10007.do'.format(SRT_HOST)
SRT_RESERVE = '{}/arc/selectListArc05013.do'.format(SRT_HOST)

EMAIL_REGEX = re.compile(r"[^@]+@[^@]+\.[^@]+")
PHONE_NUMBER_REGEX = re.compile(r"(\d{3})-(\d{3,4})-(\d{4})")

class Srt(object):
    def __init__(self, srt_id, srt_pwd, auto_login=True):
        self.srt_id = srt_id
        self.srt_pwd = srt_pwd
        self.logined = False
        self.reserved = False
        self.reservations = []

        if auto_login:
            self.login(srt_id, srt_pwd)

    def __repr__(self):
        return "[Srt object] {}".format(self.srt_id)

    def _result_check(self, response):
        if find_col_elem_text(response, 'strResult') == 'SUCC':
            return True
        
        else:
            message = find_col_elem_text(response, 'msgTxt')
            description = find_col_elem_text(response, 'MSG')

            if find_col_elem_text(response, 'msgCd') == 'S111':
                raise NeedToLoginError(message)
            else:
                raise SrtError(message, description)

    def login(self, srt_id=None, srt_pwd=None):
        if srt_id is None:
            srt_id = self.srt_id
        if srt_pwd is None:
            srt_pwd = self.srt_pwd

        if EMAIL_REGEX.match(srt_id):
            login_code = '2'
        elif PHONE_NUMBER_REGEX.match(srt_id):
            login_code = '3'
        else:
            login_code = '1'

        data = {
            'srchDvCd': login_code,
            'srchDvNm': srt_id,
            'hmpgPwdCphd': srt_pwd,
        }
        response = request(SRT_LOGIN, data, 
                           os.path.join(os.getcwd(), 'src/login.xml'))
        
        if self._result_check(response):
            self.membership_number = find_col_elem_text(response, 'MB_CRD_NO')
            self.kr_session_id = find_col_elem_text(response, 'KR_JSESSIONID')
            self.sr_session_id = find_col_elem_text(response, 'SR_JSESSIONID')

            self.logined = True
            return True

    def search(self, dep_stn_name, arr_stn_name,
               dep_date=None, dep_time=None, 
               srt_only=True, include_no_seat=False, train_type='전체'):
        if dep_date is None:
            dep_date = datetime.now().strftime('%Y%m%d')
            dep_time = datetime.now().strftime('%H%M%S') 
        elif dep_date is not None and dep_time is None:
            dep_time = '000000'
        
        data = {
            'chtnDvCd': '1',
            'dptDt': dep_date,
            'dptTm': dep_time,
            'dptRsStnCd': get_station_code(dep_stn_name), 
            'arvRsStnCd': get_station_code(arr_stn_name),
            'stlbTrnClsfCd': get_train_code(train_type),
            'trnGpCd': get_train_group_code(train_type),
            'psgNum': '1',          # need to update
            'seatAttCd': '015',     # need to update
            'arriveTime': 'N',
        }
        response = request(SRT_SEARCH, data, 
                           os.path.join(os.getcwd(), 'src/search_without_login.xml'))

        if self._result_check(response):
            dataset = find_other_elem(response, 'Dataset[@id="dsOutput1"]', 1)
            rows = find_other_elem(dataset, 'Row', 2)
            trains = []
            for row in rows:
                train = Train(row)
                trains.append(train)

            if srt_only:
                trains = filter(lambda x: x.train_name == 'SRT' in trains)

            if not include_no_seat:
                trains = filter(lambda x: x.has_seat() in trains)

            return trains

    def reserve(self, train):
        if not self.logined:
            raise Exception("로그인 후 사용하십시오.")
        
        elif train.train_name != 'SRT':
            raise Exception("SRT만 예약 가능합니다.")

        else:
            data = {
                'runDt1': train.dep_date,
                'trnNo1': "{0:0>5}".format(train.train_no),
                'dptDt1': train.dep_date,
                'dptTm1': train.dep_time,
                'dptRsStnCd1': train.dep_stn_code,
                'dptRsStnCdNm1': train.dep_stn_name,
                'arvRsStnCd1': train.arr_stn_code,
                'arvRsStnCdNm1': train.arr_stn_name,

                'MB_CRD_NO': self.membership_number,
                'ABRD_RS_STN_CD': train.dep_stn_code,
                'GOFF_RS_STN_CD': train.arr_stn_code,
                'KR_JSESSIONID': self.kr_session_id,
                'SR_JSESSIONID': self.sr_session_id,
            }
            response = request(SRT_RESERVE, data, 
                               os.path.join(os.getcwd(), 'src/reserve.xml'))

            for attempt in range(2):
                try:
                    self._result_check(response)
                except NeedToLoginError:
                    print("NeedToLoginError")
                    self.login()
                    response = request(SRT_RESERVE, data, 
                                    os.path.join(os.getcwd(), 'src/reserve.xml'))
                else:
                    break

            self.reserved = True

            dataset = find_other_elem(response, 'Dataset[@id="dsOutput2"]', 1)
            rows = find_other_elem(dataset, 'Row', 2)
            tickets = []
            for row in rows:
                ticket = Ticket(row)
                tickets.append(ticket)
            
            data = {
                'reservation_number': find_col_elem_text(response, 'pnrNo'),
                'journey_count': find_col_elem_text(response, 'jrnyCnt'),
                'total_price': find_col_elem_text(response, 'totRcvdAmt'),
            }
            reservation = Reservation(train, tickets, data)
            self.reservations.append(reservation)

            return reservation

    def remove_cancelled_reservation(self):
        for reservation in self.reservations:
            if not reservation.is_available:
                self.reservations.pop(reservation)
