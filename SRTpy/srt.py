from config import *
from datetime import datetime
from xml.etree import ElementTree as ET
import os, re

from train import *
from tree import *

SRT_HOST = 'https://app.srail.co.kr'
SRT_LOGIN = '{}/apb/selectListApb01080.do'.format(SRT_HOST)
SRT_LOGOUT = '{}/apb/selectListApb01081.do'.format(SRT_HOST)
SRT_SEARCH = '{}/ara/selectListAra10007.do'.format(SRT_HOST)

EMAIL_REGEX = re.compile(r"[^@]+@[^@]+\.[^@]+")
PHONE_NUMBER_REGEX = re.compile(r"(\d{3})-(\d{3,4})-(\d{4})")

class Srt(object):
    
    _device_key = DEVICE_KEY
    _device_OS = 'iOS'
    _device_info = 'iPhone&#32;OS&#32;10.2&#32;iPhone'

    def __init__(self, srt_id, srt_pwd, auto_login=True):
        self.srt_id = srt_id
        self.srt_pwd = srt_pwd
        self.logined = False
        if auto_login:
            self.login(srt_id, srt_pwd)
        
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

        url = SRT_LOGIN
        data = {
            'srchDvCd': login_code,
            'srchDvNm': srt_id,
            'hmpgPwdCphd': srt_pwd,
            'deviceKey': self._device_key,
            'strOS': self._device_OS,
            'strDeviceInfo': self._device_info
        }

        tree = ET.parse(os.path.join(os.getcwd(), 'src/login.xml'))
        response = request(tree.getroot(), url, data)
        
        if find_elem(response, 'strResult').text == 'SUCC':
            self.name = find_elem(response, 'CUST_NM').text
            self.membership_number = find_elem(response, 'MB_CRD_NO').text
            self.phone_number = find_elem(response, 'MBL_PHONE').text

            self.logined = True
            return True
        else:
            self.logined = False
            print(find_elem(root, 'MSG').text)
            return False

    def search(self, dep_stn_name, arr_stn_name, dep_date=None, dep_time=None, train_type='전체'):

        if dep_date is None:
            dep_date = datetime.now().strftime('%Y%m%d')
            dep_time = datetime.now().strftime('%H%M%S') 
        elif dep_date is not None and dep_time is None:
            dep_time = '000000'
        
        url = SRT_SEARCH
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
            'strOS': self._device_OS,
            'strDeviceInfo': self._device_info
        }

        tree = ET.parse(os.path.join(os.getcwd(), 'src/search_without_login.xml'))
        response = request(tree.getroot(), url, data)

        # need to update
        # process response data by using Train object
        return response
