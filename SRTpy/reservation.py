from tree import *
from datetime import datetime, timedelta
from constants import SEAT_OPTIONS

class Ticket(object):
    def __init__(self, data):
        self.price = find_col_elem(data, 'rcvdAmt').text
        self.original_price = find_col_elem(data, 'seatPrc').text
        self.reduced_price = find_col_elem(data, 'dcntAmt').text

        self.seat_type = '일반실' if find_col_elem(data, 'psrmClCd').text == '1' else '특실'
        self.seat_option = SEAT_OPTIONS.get(find_col_elem(data, 'rqSeatAttCd').text)

        self.car_number = find_col_elem(data, 'scarNo').text
        self.seat_number = find_col_elem(data, 'seatNo').text

    def __repr__(self):
        repr_str = "{} {}호차 {}, {}원".format(
            self.seat_type,
            self.car_number,
            self.seat_number,
            self.price,
        )

        return repr_str

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
        repr_str = "{} {}매, {}원".format(
            train_information, 
            len(self.tickets),
            self.total_price,
        )

        return repr_str

    def is_available(self):
        return datetime.now() < self.cancel_time
