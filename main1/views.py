from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def welcome_view(request):
    return HttpResponse("Hi, this is the main page for phone review!")
