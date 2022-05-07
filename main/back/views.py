from django.shortcuts import render , redirect

# Create your views here.
def component(request):
    return render(request, 'home.html')