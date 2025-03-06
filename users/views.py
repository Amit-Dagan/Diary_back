from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth.models import User


def login_user(request):
    if request.method == 'POST':
        pass

    else: return(request, {})


def signin_user(request):
    u = User.objects.get(username="john")
    u.set_password("new password")
    u.save()