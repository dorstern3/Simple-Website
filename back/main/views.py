from django.shortcuts import render
from django.http import HttpResponse
# from .forms import customerform
# Create your views here.


def form(request):
    # form = customerform()
    # context={'form':form}
    return render(request,'index.html')


def index(response):
    return HttpResponse("index page")

def home(response):
    return HttpResponse("home page")