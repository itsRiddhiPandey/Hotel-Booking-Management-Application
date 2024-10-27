# forms.py
from django import forms
from django.contrib.auth.models import User
from .models import Profile

class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['phone_number', 'gender','address', 'date_of_birth','profile_pic']

class UpdateUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']
