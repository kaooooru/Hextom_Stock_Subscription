from django.shortcuts import render, redirect
from .forms import SubscripForm
from .models import Subscription
from django.http import HttpResponse, Http404
from django.contrib import messages 
from twilio.rest import Client

import requests
from bs4 import BeautifulSoup
import requests_html
import lxml.html as lh
import re
import time

def index(request):
    records = Subscription.objects.all()
    if request.method == 'POST':
        if 'sendnow' in request.POST:
            return broadcast(request)
        elif 'subscribe' in request.POST:
            form = SubscripForm(request.POST)
            if form.is_valid():        
                form.save()
                return redirect('stocksub:thanks')
        elif 'unsubscribe' in request.POST:
            current_ticker = request.POST.get('ticker')
            current_phonenum = request.POST.get('number')
            try:
                user = Subscription.objects.get(ticker=current_ticker, number=current_phonenum)
                user.delete()
            except:
                return HttpResponse("Subscription does not exist, please go back and retry.")
            return HttpResponse("Unsubscribe")

    else:
        form = SubscripForm()
    return render(request, 'stocksub/index.html', { 'form': form, 'records': records })

  

def thanks(request):
    return render(request, 'stocksub/thanks.html')

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


def broadcast(request):
    account_sid = "XXXX"
    auth_token  = "XXXX"

    client = Client(account_sid, auth_token)

    ticker = request.POST.get('ticker')

    message_to_broadcast = ("The stock price of " + ticker + " is " + str(stockPrice(ticker)))

    client.messages.create(
        to=request.POST.get('number'), 
        from_="XXXX",
        body=message_to_broadcast)
    
    return HttpResponse("messages sent!")

    
