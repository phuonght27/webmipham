# forms.py
from django import forms
from django.contrib.auth.models import User
from .models import Customer

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [ 'email','username',]

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['address', 'phone']
