from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from stale import views


# Create your views here.


# request pages


def about(request):
    return render(request, 'about.html', {})


def contact(request):
    if request.method == "POST":
        contactName = request.POST['contactName']
        contactEmail = request.POST['contactEmail']
        contactSubject = request.POST['contactSubject']
        contactMessage = request.POST['contactMessage']

        # send an email

        send_mail(
            'Message from: ' + contactName + ', subject: ' + contactSubject,  # subject
            contactMessage,  # message
            settings.EMAIL_HOST_USER,  # from email
            ['nsbrathwaite18@outlook.com'],  # to email
            fail_silently=False
        )

        return render(request, 'contact.html', {'contactName': contactName})
    else:
        return render(request, 'contact.html', {})


def gallery(request):
    return render(request, 'gallery.html', {})


def index(request):
    return render(request, 'index.html', {})


def services(request):
    return render(request, 'services.html', {})
