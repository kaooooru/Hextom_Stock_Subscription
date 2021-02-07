import requests
from bs4 import BeautifulSoup
import requests_html
import lxml.html as lh
import re
import time

ticker = 'AAPL'

url = 'https://in.finance.yahoo.com/quote/' + ticker
session = requests_html.HTMLSession()
r = session.get(url)
content = BeautifulSoup(r.content, 'lxml')
try:
    price = str(content).split('data-reactid="32"')[4].split('</span>')[0].replace('>','')
except IndexError as e:
    price = 0.00
price = price or "0"
try:
    price = float(price.replace(',',''))
except ValueError as e:
    price = 0.00
time.sleep(1)
print(price)