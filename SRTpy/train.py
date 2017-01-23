"""
    SRTpy -- SRT (https://etk.srail.co.kr) wrapper for Python.
    ==========================================================

    : copyright: (c) 2017 by Heena Kwag.
    : URL: <http://github.com/dotaitch/SRTpy>
    : license: BSD, see LICENSE for more details.
"""

from datetime import datetime
from xml.etree import ElementTree as ET

from .utils import *
from .constants import TRAIN_CODE, TRAIN_GROUP_CODE, STATION_CODE
    
class Train(object):
    def __init__(self, data):
        self.train_code = find_col_elem_text(data, 'stlbTrnClsfCd')
        self.train_name = TRAIN_CODE.get(self.train_code)
        self.train_group_code = find_col_elem_text(data, 'trnGpCd')
        self.train_no = find_col_elem_text(data, 'trnNo')

        self.dep_date = find_col_elem_text(data, 'dptDt')
        self.dep_time = find_col_elem_text(data, 'dptTm')
        self.dep_stn_code = find_col_elem_text(data, 'dptRsStnCd')
        self.dep_stn_name = STATION_CODE.get(self.dep_stn_code)

        self.arr_date = find_col_elem_text(data, 'arvDt')
        self.arr_time = find_col_elem_text(data, 'arvTm')
        self.arr_stn_code = find_col_elem_text(data, 'arvRsStnCd')
        self.arr_stn_name = STATION_CODE.get(self.arr_stn_code)

        self.special_seat_str = find_col_elem_text(data, 'sprmRsvPsbStr')
        self.general_seat_str = find_col_elem_text(data, 'gnrmRsvPsbStr')

    def get_information(self):
        dep_date = "{}월{}일".format(self.dep_date[4:6], self.dep_date[6:])
        dep_time = "{}:{}".format(self.dep_time[:2], self.dep_time[2:4])
        arr_time = "{}:{}".format(self.arr_time[:2], self.arr_time[2:4])

        information = "[{} {}] {} {}({})->{}({})".format(
            self.train_name,
            self.train_no,
            dep_date,
            self.dep_stn_name,
            dep_time,
            self.arr_stn_name,
            arr_time,
        )

        return information

    def __repr__(self):
        repr_str = self.get_information()

        message = " "
        if self.special_seat_str != "-":
            message += "특실 " + self.special_seat_str + " / "
        message += "일반실 " + self.general_seat_str

        return repr_str + message

    def has_special_seat(self):
        return "예약" in self.special_seat_str

    def has_general_seat(self):
        return "예약" in self.general_seat_str

    def has_seat(self):
        return self.has_special_seat() or self.has_general_seat()
