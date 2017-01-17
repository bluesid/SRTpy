from tree import *
from datetime import datetime, timedelta
from constants import SEAT_OPTIONS

class Reservation(object):
    def __init__(self, train, data):
        self.train = train

        self.price = find_col_elem(data, 'rcvdAmt').text
        self.original_price = find_col_elem(data, 'seatPrc').text
        self.reduced_price = find_col_elem(data, 'dcntAmt').text

        self.seat_type = '일반실' if find_col_elem(data, 'psrmClCd').text == '1' else '특실'
        self.seat_option = SEAT_OPTIONS.get(find_col_elem(data, 'rqSeatAttCd').text)

        self.car_number = find_col_elem(data, 'scarNo').text
        self.seat_number = find_col_elem(data, 'seatNo').text

        self.buy_time = datetime.now()
        self.cancel_time = self.buy_time + timedelta(minutes=20)

    def __repr__(self):
        train_information = self.train.get_information()
        
        repr_str = "{} {} {}호차 {}, {}원".format(
            train_information,
            self.seat_type,
            self.car_number,
            self.seat_number,
            self.price,
        )

        return repr_str

    def is_available(self):
        return datetime.now() < self.cancel_time
