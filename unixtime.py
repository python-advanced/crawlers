import requests
from bs4 import BeautifulSoup

data = {'timestamp': '1598641153', 'Submit': 'Convert'}

r = requests.post('https://www.unixtimestamp.com/index.php', data=data)
if r.status_code == requests.codes.ok:
    soup = BeautifulSoup(r.text, 'html.parser')
    print(soup.prettify())
   