from django.db.models import Q
from django.views.generic import TemplateView, DetailView, ListView
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


class Buscar(ListView):
    template_name = 'buscar.html'
    model = Noticia
    context_object_name = 'noticias'

    def get_queryset(self):
        queryset = super(Buscar, self).get_queryset()
        termino = self.request.GET.get('termino', '')

        if not termino:
            return queryset.none()

        queryset = queryset.filter(
            Q(titular__icontains=termino) |
            Q(contenido__icontains=termino) |
            Q(sumilla__icontains=termino)
        )

        return queryset
