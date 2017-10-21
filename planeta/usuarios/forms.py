from django import forms
from django.contrib.auth.forms import UserCreationForm


class RegistroForm(UserCreationForm):
    nombres = forms.CharField(required=True)
    apellidos = forms.CharField(required=True)
