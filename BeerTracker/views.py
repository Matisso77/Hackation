from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import get_token, csrf_exempt, requires_csrf_token
from django.conf import settings
from django.shortcuts import redirect


def index(request):
    return HttpResponse("Siemano")