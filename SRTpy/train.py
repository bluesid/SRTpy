from constants import *
from datetime import datetime
from xml.etree import ElementTree as ET

from tree import *
    
def get_train_code(train_type_name):
    for k, v in TRAIN_CODE.items():
        if v == train_type_name:
            return k

def get_train_group_code(train_type_name):
    for k, v in TRAIN_GROUP_CODE.items():
        if train_type_name in v:
            return k

def get_station_code(station_name):
    for k, v in STATION_CODE.items():
        if v == station_name:
            return k

class Train(object):
    def __init__(self, data):
        self.train_code = find_col_elem(data, 'stlbTrnClsfCd').text
        self.train_name = TRAIN_CODE.get(self.train_code)
        self.train_group_code = find_col_elem(data, 'trnGpCd').text
        self.train_no = find_col_elem(data, 'trnNo').text

        self.dep_date = find_col_elem(data, 'dptDt').text
        self.dep_time = find_col_elem(data, 'dptTm').text
        self.dep_stn_code = find_col_elem(data, 'dptRsStnCd').text
        self.dep_stn_name = STATION_CODE.get(self.dep_stn_code)

        self.arr_date = find_col_elem(data, 'arvDt').text
        self.arr_time = find_col_elem(data, 'arvTm').text
        self.arr_stn_code = find_col_elem(data, 'arvRsStnCd').text
        self.arr_stn_name = STATION_CODE.get(self.arr_stn_code)

        self.special_seat_str = find_col_elem(data, 'sprmRsvPsbStr').text
        self.general_seat_str = find_col_elem(data, 'gnrmRsvPsbStr').text

    def __repr__(self):
        dep_date = "{}월{}일".format(self.dep_date[4:6], self.dep_date[6:])
        dep_time = "{}:{}".format(self.dep_time[:2], self.dep_time[2:4])
        arr_time = "{}:{}".format(self.arr_time[:2], self.arr_time[2:4])

        message = ""
        if self.special_seat_str != "-":
            message += "특실 " + self.special_seat_str + " / "
        message += "일반실 " + self.general_seat_str

        repr_str = "[{} {}] {}, {}({})->{}({}) {}".format(
            self.train_name,
            self.train_no,
            dep_date,
            self.dep_stn_name,
            dep_time,
            self.arr_stn_name,
            arr_time,
            message
        )

        return repr_str

    def has_special_seat(self):
        return "예약" in self.special_seat_str

    def has_general_seat(self):
        return "예약" in self.general_seat_str
