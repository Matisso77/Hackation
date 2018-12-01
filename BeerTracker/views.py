import requests
import json
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import get_token, csrf_exempt, requires_csrf_token
from django.conf import settings
from django.shortcuts import redirect
from .models import Bar, Beers, Stock
from scraper import getData


def index(request):
    return render(request, 'Index.html')

def shit(request):
    response_json = []
    for bar in Bar.objects.all():
        stock = []
        for stocks in Stock.objects.all().filter(Bar=bar.id):
            item = stocks.Beer.Name
            stock.append({"beer_name": item,
                          "bigCost": stocks.bigCost,
                          "smallCost": stocks.smallCost})
        response_json.append({"name": bar.Name,
                              "localization": bar.Localization,
                              "google_id": bar.google_id,
                              "stock": stock})

    return HttpResponse(json.dumps(response_json, indent=2, separators=(',', ': ')),
                        content_type="application/json")

def map(request):
    local = request.POST.get("LocField")

    return render(request, 'Map.html', {"local": local, })

