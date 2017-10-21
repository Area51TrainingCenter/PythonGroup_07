from django.db.models import Q
from django.shortcuts import redirect
from django.views.generic import TemplateView, DetailView, ListView, FormView
from noticias.models import Noticia, Categoria as CategoriaModel
from website.forms import ComentarioForm


class Home(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        contexto = super(Home, self).get_context_data(**kwargs)
        contexto['nombre'] = 'Planeta'
        contexto['noticias'] = Noticia.objects.all().order_by('-fecha_publicacion')[:5]
        return contexto


class DetalleNoticia(DetailView, FormView):
    template_name = 'detalle.html'
    model = Noticia
    context_object_name = 'noticia'
    form_class = ComentarioForm
    # success_url = '??????'

    def form_valid(self, form):
        comentario = form.save(commit=False)
        comentario.usuario = self.request.user
        comentario.noticia = self.get_object()
        comentario.save()
        return redirect('detalle', pk=self.get_object().pk)

    def get_context_data(self, **kwargs):
        contexto = super(DetalleNoticia, self).get_context_data(**kwargs)
        contexto['comentarios'] = self.get_object().comentario_set.order_by('-fecha_publicacion')
        return contexto


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


class Categoria(ListView):
    template_name = 'categoria.html'
    model = Noticia
    context_object_name = 'noticias'

    def get_context_data(self, **kwargs):
        contexto = super(Categoria, self).get_context_data(**kwargs)
        contexto['categoria'] = CategoriaModel.objects.get(pk=self.kwargs['pk'])
        return contexto

    def get_queryset(self):
        return Noticia.objects.filter(categoria__pk=self.kwargs['pk']).order_by('-fecha_publicacion')
