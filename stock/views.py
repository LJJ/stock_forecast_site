# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json

from django.shortcuts import render


# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    stocks = ["YHOO", "GOOG", "BABA", "NTES", "TCEHY"]
    return render(request, "home.html",{'stocks': json.dumps(stocks)})