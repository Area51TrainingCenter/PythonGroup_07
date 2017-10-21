from django.contrib.auth import login
from django.views.generic import FormView

from usuarios.forms import RegistroForm


class Registro(FormView):
    template_name = 'registro.html'
    form_class = RegistroForm
    success_url = '/'

    def form_valid(self, form):
        # data = form.cleaned_data
        # usuario = User()
        # usuario.first_name = data['nombres']
        # usuario.last_name = data['apellidos']
        # usuario.username = data['username']
        # usuario.set_password(data['password1'])
        # usuario.save()

        usuario = form.save()
        login(self.request, usuario, 'django.contrib.auth.backends.ModelBackend')

        return super(Registro, self).form_valid(form)
