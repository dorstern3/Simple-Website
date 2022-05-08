from django.shortcuts import render , redirect
from django.http import HttpResponse
# Create your views here.

# Home page
def Home(request):
    return render(request,'Home.html')

# SignUp page
def SignUp(request):
    return render(request,'SignUp.html')
