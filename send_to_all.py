import psycopg2
from twilio.rest import Client
import requests
from bs4 import BeautifulSoup
import requests_html
import lxml.html as lh
import re
import time

def stockPrice(ticker):
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
    return price

def broadcast(ticker, number, price):
    account_sid = "ACa2a8034dadd2bd364d00a64187ae037c"
    auth_token  = "75f5feebbb1a43ed1a602e76709e0982"

    client = Client(account_sid, auth_token)

    message_to_broadcast = ("The stock price of " + ticker + " is " + str(price))

    client.messages.create(
        to=number, 
        from_="+16479059186",
        body=message_to_broadcast)

try:
    connection = psycopg2.connect(user="vickyhhuang",
                                  password="0424",
                                  host="",
                                  port="",
                                  database="stocksub")
    cursor = connection.cursor()
    postgreSQL_select_Query = "select * from stocksub_subscription"

    cursor.execute(postgreSQL_select_Query)
    subscribe_records = cursor.fetchall() 

    for row in subscribe_records:
        broadcast(row[1], row[2], stockPrice(row[1]))
    
    print("Sent!")


except (Exception, psycopg2.Error) as error :
    print ("Error while fetching data from PostgreSQL", error)

finally:
    if(connection):
        cursor.close()
        connection.close()
