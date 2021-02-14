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

from django.shortcuts import render
from django.http import HttpResponse
# Create your views here
from stale.models import *
from stale.forms import StaffForm


def home(request):
    return render(request, 'Main/index.html', {})


def animals(request):
    animal = Animal.objects.all()

    total_animals = animal.count()
    context = {'animal': animal, 'total_animals': total_animals}
    return render(request, 'Main/animal.html', context)


def species(request):
    specie = Species.objects.all()
    return render(request, 'Main/species.html', {'specie': specie})


def staff(request):
    staffs = Staff.objects.all()

    total_staff = staffs.count()
    context = {'total_staff': total_staff, 'staffs': staffs}
    return render(request, 'Main/staff.html', context)


def member(request, pk):
    staffs = Staff.objects.get(id=pk)

    context = {'staffs': staffs}
    return render(request, 'Main/staffedit.html', context)


def createstaff(request):
    form = StaffForm(request.POST)
    if request.method == 'POST':
        print('Printing POST:', request.POST)

        context = {'form': form}
        return render(request, 'Main/staff.html', context)
    else:
        return render(request, 'Main/staff.html', {})
