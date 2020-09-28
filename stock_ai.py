import requests
import pprint


r = requests.get('https://chart.stock-ai.com/history?symbol=%5ETWII&resolution=D&from=1564604150&to=1598818610', verify=False)
if r.status_code == requests.codes.ok:
    data = r.json()
    zipped = zip(data['t'], data['o'], data['h'], data['l'], data['o'], data['v'])

    pprint.pprint(list(zipped))