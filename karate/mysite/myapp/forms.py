from django import forms 
from .models import Gym,Account
from django.contrib.auth.models import User

class SignupForm(forms.Form):
    username=forms.CharField(max_length=255)
    email=forms.EmailField()
    password=forms.CharField(max_length=255)

class CoachForm(forms.ModelForm):
    class Meta:
        model=Gym
        fields=['coach_name','time','location','level','coach_level','price']

class LoginForm(forms.Form):
    username=forms.CharField(max_length=255)
    password=forms.CharField(max_length=255)