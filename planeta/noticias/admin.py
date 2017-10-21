from django.contrib import admin

from noticias.models import Noticia, Categoria, Comentario


class NoticiaAdmin(admin.ModelAdmin):
    list_display = ('titular', 'sumilla', 'fecha_publicacion',)
    list_display_links = list_display
    search_fields = ('titular', 'sumilla', 'contenido',)
    list_filter = ('fecha_publicacion',)


class ComentarioAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'noticia', 'texto',)
    list_display_links = list_display


admin.site.register(Noticia, NoticiaAdmin)
admin.site.register(Categoria)
admin.site.register(Comentario, ComentarioAdmin)
