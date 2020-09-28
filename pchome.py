import requests
import pprint
import re


r = requests.get('https://ecshweb.pchome.com.tw/search/v3.3/all/results?q=%E6%9B%B2%E9%9D%A2%E8%9E%A2%E5%B9%95&page=1&sort=sale/dc')
if r.status_code == requests.codes.ok:
    data = r.json()
    pprint.pprint(data)
    for product in data['prods']:
        print(product['name'])
        print(product['price'])
