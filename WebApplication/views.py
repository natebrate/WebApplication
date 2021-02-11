"""
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Place the redirection of response to the appropriate page
"""

from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings


def home(request):
    return render(request, 'index.html', {})


def animals(request):
    return render(request, 'animal.html', {})


def species(request):
    return render(request, 'species.html', {})


def staff(request):
    return render(request, 'staff.html', {})
