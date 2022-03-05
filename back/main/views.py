from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(response):
    return HttpResponse("index page")

def home(response):
    return HttpResponse("home page")
