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
    bar = Bar.objects.get.all()

    return HttpResponse({"name": 123}, indent=2, separators=(',', ': '),
                        content_type="application/json")

def map(request):
    local = request.POST.get("LocField")

    return render(request, 'Map.html', {"local": local, })

