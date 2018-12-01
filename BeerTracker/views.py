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

def map(request):
    return  render(request, 'Map.html')

def add(request):
    try:
        for item in getData():
            bar = Bar()
            bar.Link = item[0]
            bar.Name = item[1]

        return HttpResponse("elo")
    except Exception as ex:
        return render(request, HttpResponse('dupa'))
