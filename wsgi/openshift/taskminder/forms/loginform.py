__author__ = 'Q'
from django import forms

class LogInForm(forms.Form):
    username = forms.CharField(max_length=200)
    password = forms.CharField(max_length=200,widget=forms.PasswordInput)
