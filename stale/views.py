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

from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here
from stale.models import *
from stale.forms import StaffForm, SpeciesForm, AnimalForm


def home(request):
    return render(request, 'Main/index.html', {})


def fronts(request):
    return render(request, 'index.html', {})


# ================== ANIMAL PROCEDURES ====================
def animals(request):
    animal = Animal.objects.all()

    total_animals = animal.count()
    context = {'animal': animal, 'total_animals': total_animals}
    return render(request, 'Main/animal.html', context)


def updateanimal(request, pk):
    animal = Animal.objects.get(id=pk)
    form = AnimalForm(instance=animal)

    if request.method == 'POST':
        form = AnimalForm(request.POST, instance=animal)
        if form.is_valid():
            form.save()
            return redirect('/animals/')

    context = {'form': form}
    return render(request, 'Main/animalForm.html', context)


def deleteanimal(request, pk):
    deletes = Animal.objects.get(id=pk)
    if request.method == "POST":
        deletes.delete()
        return redirect('/animal')

    context = {'deletes': deletes}
    return render(request, 'Main/animal.html', context)


def createanimal(request):
    form = AnimalForm(request.POST)
    if form.is_valid():
        animal = form.save(commit=False)
        animal.user = request.user
        animal.save()
        content = form.clean()
        context = {'form': form, 'content': content}
        return render(request, 'Main/animalForm.html', context)
    else:
        context = {'form': form}
        return render(request, 'Main/animalForm.html', context)


# ================ SPECIES PROCEDURES ========================
def species(request):
    specie = Species.objects.all()

    total_species = specie.count()
    context = {'specie': specie, 'total_species': total_species}
    return render(request, 'Main/species.html', context)


def createspecies(request):
    form = SpeciesForm(request.POST)
    if form.is_valid():
        specie = form.save(commit=False)
        specie.user = request.user
        specie.save()
        content = form.clean()
        context = {'form': form, 'content': content}
        return redirect('/species/')
    else:
        context = {'form': form}
        return render(request, 'Main/speciesForm.html', context)


def updatespecies(request, pk):
    specie = Species.objects.get(id=pk)
    form = SpeciesForm(instance=specie)

    if request.method == 'POST':
        form = SpeciesForm(request.POST, instance=specie)
        if form.is_valid():
            form.save()
            return redirect('/species/')

    context = {'form': form}
    return render(request, 'Main/speciesForm.html', context)


def deletespecies(request, pk):
    deletes = Species.objects.get(id=pk)
    if request.method == "POST":
        deletes.delete()
        return redirect('/species')

    context = {'deletes': deletes}
    return render(request, 'Main/species.html', context)


# ============== STAFF STUFF ======================
def staff(request):
    staffs = Staff.objects.all()

    total_staff = staffs.count()
    context = {'total_staff': total_staff, 'staffs': staffs}
    return render(request, 'Main/staff.html', context)


def createstaff(request):
    form = StaffForm(request.POST)
    if form.is_valid():
        user = form.save(commit=False)
        user.user = request.user
        user.save()
        content = form.clean()
        context = {'form': form, 'content': content}
        return render(request, 'Main/staffForm.html', context)
    else:
        context = {'form': form}
        return render(request, 'Main/staffForm.html', context)


def updatestaff(request, pk):
    staffer = Staff.objects.get(id=pk)
    form = StaffForm(instance=staffer)

    if request.method == 'POST':
        form = StaffForm(request.POST, instance=staffer)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'Main/staffForm.html', context)


# Has not be added to webpage as you dont delete but rather archive
def deletestaff(request, pk):
    deletes = Staff.objects.get(id=pk)
    if request.method == "POST":
        deletes.delete()
        return redirect('/')

    context = {'deletes': deletes}
    return render(request, 'Main/staff.html', context)
