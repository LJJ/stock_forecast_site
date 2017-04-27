# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json
from stock.models import History


from django.shortcuts import render


# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    stocks = ["YHOO", "GOOG", "BABA", "NTES", "TCEHY"]
    return render(request, "home.html",{'stocks': json.dumps(stocks)})

def select(request):
    stock_id = request.GET['stock_id']
    info = History.objects.filter(symbol=stock_id)[:300]
    result = []
    for item in info:
        dict = {"date":str(item.time),"value":item.close,"volume":item.volume}
        result.append(dict)
    return render(request,"stock.html",{'info':json.dumps(result)})