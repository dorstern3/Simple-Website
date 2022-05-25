from django.shortcuts import render , redirect
from django.http import HttpResponse

# SignUp & Login
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm

# Email
from .forms import UserRegisterEmail

# SubscribeForm
from .forms import SubscribeForm

# Create your views here.

# SignUp page
def SignUp(request):
 if request.method == "GET":
        print("that request.method GET")
        return render(request,'SignUp.html')

 if request.method == "POST":
        print("that request.method POST")
        # form=UserCreationForm(request.POST)
        form=UserRegisterEmail(request.POST)
        print(form.is_valid())
        print(form.errors)
        if form.is_valid():
            print("form.is_valid")
            form.save()
            print("form.save")
            email=form.cleaned_data.get('email')
            print(email)
            username=form.cleaned_data.get('username')
            print(username)
            password=form.cleaned_data.get('password1')
            print(password)
            user=authenticate(username=username, password=password,email=email)
            print(user)
            print("user")
            login(request, user)
            print(login(request, user))
            print("login")
            return redirect('ThankYouPageSignUp')

        else:
            print("that no work")
            return render(request, 'SignUp.html')

 else:
        # if request.method == "GET":
        print("that request.method GET")
        return render(request, 'SignUp.html')


# Home page
def Home(request):
    if request.method == "GET":
        print("that request.method GET")
        return render(request, 'Home.html')

    if request.method == "POST":
        print("that request.method POST")
        username=request.POST.get('username')
        print(username)
        password=request.POST.get('password')
        print(password)
        user=authenticate(username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            print(login(request, user))
            return redirect('ThankYouPageSignIn')

        else:
            return render(request,'Home.html')
    

# Contact page
def Contact(request):
    if request.method == "GET":
        print("that request.method GET")
        return render(request,'Contact.html')

    if request.method == "POST":
        print("that request.method POST")
        sub=SubscribeForm(request.POST)
        print(sub.errors)
        if sub.is_valid():
            print("sub valid")
            sub.save()
            print("sub.save")
            return redirect('Contact')
        else:
            print("sub not valid")
            return render(request,'Contact.html')






# About page
def About(request):
    return render(request,'About.html')

# ThankYouPageSignIn page
def ThankYouPageSignIn(request):
    return render(request,'ThankYouPageSignIn.html')

# ThankYouPageSignUp page
def ThankYouPageSignUp(request):
    return render(request,'ThankYouPageSignUp.html')
