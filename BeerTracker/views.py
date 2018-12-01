import json
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import get_token, csrf_exempt, requires_csrf_token
from django.conf import settings
from django.shortcuts import redirect
from .models import *
from scraper import getData


def index(request):
    return HttpResponse("Siemano")


def add(request):
    try:
        received_json_data = json.loads(request.body)
        return HttpResponse(received_json_data)
    except Exception as ex:
        return render(request, HttpResponse('dupa'))
