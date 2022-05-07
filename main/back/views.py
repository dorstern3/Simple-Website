from django.shortcuts import render , redirect
from django.http import HttpResponse
# Create your views here.
def Home(request):
    return render(request,'Test.html')