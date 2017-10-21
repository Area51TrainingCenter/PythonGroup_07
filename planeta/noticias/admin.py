from django.contrib import admin

from noticias.models import Noticia, Categoria


class NoticiaAdmin(admin.ModelAdmin):
    list_display = ('titular', 'sumilla', 'fecha_publicacion',)
    list_display_links = list_display
    search_fields = ('titular', 'sumilla', 'contenido',)
    list_filter = ('fecha_publicacion',)


admin.site.register(Noticia, NoticiaAdmin)
admin.site.register(Categoria)
