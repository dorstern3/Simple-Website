from django import forms

# Email input
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


# UserRegisterEmail
class UserRegisterEmail(UserCreationForm):
    email=forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']