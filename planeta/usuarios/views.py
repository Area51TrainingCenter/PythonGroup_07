from django.views.generic import FormView

from usuarios.forms import RegistroForm


class Registro(FormView):
    template_name = 'registro.html'
    form_class = RegistroForm
