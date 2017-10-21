"""planeta URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from website.views import Home, DetalleNoticia, Buscar, Categoria
from usuarios.views import Registro, Logout, Login, Perfil

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^registro/?$', Registro.as_view(), name='registro'),
    url(r'^login/?$', Login.as_view(), name='login'),
    url(r'^logout/?$', Logout.as_view(), name='logout'),
    url(r'^perfil/?$', Perfil.as_view(), name='perfil'),

    url(r'^buscar/?$', Buscar.as_view(), name='buscar'),
    url(r'^noticias/(?P<pk>\d+)/?$', DetalleNoticia.as_view(), name='detalle'),
    url(r'^categoria/(?P<pk>\d+)/?$', Categoria.as_view(), name='categoria'),
    url(r'^$', Home.as_view(), name='home'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
