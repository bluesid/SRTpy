"""
    SRTpy -- SRT (https://etk.srail.co.kr) wrapper for Python.
    ==========================================================

    : copyright: (c) 2017 by Heena Kwag.
    : URL: <http://github.com/dotaitch/SRTpy>
    : license: BSD, see LICENSE for more details.
"""

import random
import requests
from xml.etree import ElementTree as ET

from .constants import *

def get_key_by_value(value, data):
    for k, v in data.items():
        if v == value:
            return k

def get_key_by_value_list(value, data):
    for k, v in data.items():
        if value in v:
            return k

def get_namespace(root):
    tag = root.tag
    ns = tag[tag.find('{')+1:tag.find('}')]
    return ns

def find_col_elem(root, k):
    ns = get_namespace(root)
    tag = './/{{{0}}}Col[@id="{1}"]'.format(ns, k)
    return root.find(tag)

def find_col_elem_text(root, k):
    elem = find_col_elem(root, k)
    return elem.text if elem is not None else None

def find_other_elem(root, k, flag):
    ns = get_namespace(root)
    tag = './/{{{0}}}{1}'.format(ns, k)
    if flag == 1:
        return root.find(tag)
    else:
        return root.findall(tag)

def request(url, data, filepath):
    tree = ET.parse(filepath)
    root = tree.getroot()
    ns = get_namespace(root) 
    ET.register_namespace('', ns)
    for k, v in data.items():
        elem = find_col_elem(root, k)
        elem.text = v
    tree = ET.tostring(root, 'utf-8')
    user_agent = random.choice(USER_AGENTS)
    headers = {
        'Content-Type': 'application/xml',
        'User-Agent': user_agent,
    }
    response = requests.post(url, data=tree, headers=headers).content
    return ET.fromstring(response)
