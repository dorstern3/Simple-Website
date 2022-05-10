from django.shortcuts import render , redirect
from django.http import HttpResponse
# Create your views here.

# Home page
def Home(request):
    return render(request,'Home.html')

# SignUp page
def SignUp(request):
    return render(request,'SignUp.html')

# About page
def About(request):
    return render(request,'About.html')

# Contact page
def Contact(request):
    return render(request,'Contact.html')

# ThankYouPageSignIn page
def ThankYouPageSignIn(request):
    return render(request,'ThankYouPageSignIn.html')

# ThankYouPageSignUp page
def ThankYouPageSignUp(request):
    return render(request,'ThankYouPageSignUp.html')
