from noticias.models import Categoria


def categorias(request):
    return {
        'categorias': Categoria.objects.order_by('nombre')
    }
