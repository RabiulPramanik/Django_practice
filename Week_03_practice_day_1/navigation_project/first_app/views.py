from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, "first_app/home.html")


def about(request):
    return render(request, "first_app/about.html")


def contact(request):
    return render(request, "first_app/contact.html")

