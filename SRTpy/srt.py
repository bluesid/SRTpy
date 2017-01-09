from config import *
from xml.etree import ElementTree as ET
import os, re, requests

SRT_HOST = 'https://app.srail.co.kr'
SRT_LOGIN = '{}/apb/selectListApb01080.do'.format(SRT_HOST)
SRT_LOGOUT = '{}/apb/selectListApb01081.do'.format(SRT_HOST)

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

        def findElem(root, ns, k):
            tag = './/{{{0}}}Col[@id="{1}"]'.format(ns, k)
            return root.find(tag)

        tree = ET.parse(os.path.join(os.getcwd(), 'src/login.xml'))
        root = tree.getroot()
        ns = root.tag[root.tag.find('{')+1:root.tag.find('}')]
        ET.register_namespace('', ns)
        for k, v in data.items():
            elem = findElem(root, ns, k)
            elem.text = v
        tree = ET.tostring(root, 'utf-8')
        headers = {'Content-Type': 'application/xml'}
        response= requests.post(url, data=tree, headers=headers).text
        root = ET.fromstring(response)
        ns = root.tag[root.tag.find('{')+1:root.tag.find('}')]
        if findElem(root, ns, 'strResult').text == 'SUCC':
            self.name = findElem(root, ns, 'CUST_NM').text
            self.membership_number = findElem(root, ns, 'MB_CRD_NO').text
            self.phone_number = findElem(root, ns, 'MBL_PHONE').text

            self.logined = True
            return True
        else:
            self.logined = False
            print(findElem(root, ns, 'MSG').text)
            return False
