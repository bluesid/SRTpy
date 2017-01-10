from xml.etree import ElementTree as ET
import requests

def get_namespace(root):
    tag = root.tag
    ns = tag[tag.find('{')+1:tag.find('}')]
    return ns

def find_elem(root, k):
    ns = get_namespace(root)
    tag = './/{{{0}}}Col[@id="{1}"]'.format(ns, k)
    return root.find(tag)

def find_all_elems(root, k):
    ns = get_namespace(root)
    tag = './/{{{0}}}*[@id="{1}"]'.format(ns, k)
    return root.findall(tag)

def request(root, url, data):
    ns = get_namespace(root) 
    ET.register_namespace('', ns)
    for k, v in data.items():
        elem = find_elem(root, k)
        elem.text = v
    tree = ET.tostring(root, 'unicode')
    headers = {'Content-Type': 'application/xml'}
    response = requests.post(url, data=tree, headers=headers).text
    return ET.fromstring(response)
