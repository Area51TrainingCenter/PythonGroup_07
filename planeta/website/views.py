from django.views.generic import TemplateView, DetailView
from noticias.models import Noticia


class Home(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        contexto = super(Home, self).get_context_data(**kwargs)
        contexto['nombre'] = 'Planeta'
        contexto['noticias'] = Noticia.objects.all().order_by('-fecha_publicacion')[:5]
        return contexto


class DetalleNoticia(DetailView):
    template_name = 'detalle.html'
    model = Noticia
    context_object_name = 'noticia'
