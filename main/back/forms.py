from django import forms

# Email input
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# Subscribe
from django.forms import ModelForm
from .models import Subscribe


# UserRegisterEmail
class UserRegisterEmail(UserCreationForm):
    email=forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


# SubscribeForm
class SubscribeForm(forms.ModelForm):
    first_name=forms.CharField(required=True)
    last_name=forms.CharField(required=True)
    email=forms.CharField(required=True)
    phone=forms.CharField(required=True)
    message=forms.CharField(required=True)

    class Meta:
        model = Subscribe
        fields = '__all__'