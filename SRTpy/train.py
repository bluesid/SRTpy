from constants import *
from datetime import datetime
from xml.etree import ElementTree as ET
    
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

# make Train object
