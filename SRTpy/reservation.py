"""
    SRTpy -- SRT (https://etk.srail.co.kr) wrapper for Python.
    ==========================================================

    : copyright: (c) 2017 by Heena Kwag.
    : URL: <http://github.com/dotaitch/SRTpy>
    : license: BSD, see LICENSE for more details.
"""

from datetime import datetime, timedelta

from .utils import *
from .constants import SEAT_OPTIONS

class Ticket(object):
    def __init__(self, data):
        self.price = find_col_elem_text(data, 'rcvdAmt')
        self.original_price = find_col_elem_text(data, 'seatPrc')
        self.reduced_price = find_col_elem_text(data, 'dcntAmt')

        self.seat_type = '일반실' if find_col_elem_text(data, 'psrmClCd') == '1' else '특실'
        self.seat_option = SEAT_OPTIONS.get(find_col_elem_text(data, 'rqSeatAttCd'))

        self.car_number = find_col_elem_text(data, 'scarNo')
        self.seat_number = find_col_elem_text(data, 'seatNo')

        self.passenger_code = find_col_elem_text(data, 'psgTpCd')
        self.passenger = self._get_passenger_name()

    def __repr__(self):
        repr_str = "{} {}호차{} ({}) - {}원".format(
            self.seat_type,
            self.car_number,
            self.seat_number,
            self.passenger,
            self.price,
        )

        return repr_str

    def _get_passenger_name(self):
        if self.passenger_code == '1':
            return '어른'
        elif self.passenger_code == '2':
            return '장애 1~3급'
        elif self.passenger_code == '3':
            return '장애 4~6급'
        elif self.passenger_code == '4':
            return '경로'
        elif self.passenger_code == '5':
            return '어린이'

class Reservation(object):
    def __init__(self, train, tickets, data):
        self.train = train
        self.tickets = tickets
        
        self.reservation_number = data.get('reservation_number')
        self.journey_count = data.get('journey_count')
        self.total_price = data.get('total_price')

        self.buy_time = datetime.now()
        self.cancel_time = self.buy_time + timedelta(minutes=20)

    def __repr__(self):
        train_information = self.train.get_information()
        repr_str = "{} {}매 - {}원".format(
            train_information, 
            len(self.tickets),
            self.total_price,
        )

        return repr_str

    def is_available(self):
        return datetime.now() < self.cancel_time
