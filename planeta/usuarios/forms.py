from django import forms
from django.contrib.auth.forms import UserCreationForm


class RegistroForm(UserCreationForm):
    nombres = forms.CharField(required=True)
    apellidos = forms.CharField(required=True)

    def save(self, commit=True):
        usuario = super(RegistroForm, self).save(commit=False)
        usuario.first_name = self.cleaned_data['nombres']
        usuario.last_name = self.cleaned_data['apellidos']
        usuario.save()
        return usuario
