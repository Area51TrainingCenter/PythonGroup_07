from django.db import models
from django.contrib.auth.models import User


class Categoria(models.Model):
    nombre = models.CharField(
        max_length=50,
        blank=False,
        null=False
    )

    def __str__(self):
        return self.nombre


class Noticia(models.Model):
    titular = models.CharField(
        max_length=150,
        blank=False,
        null=False  # '' != None
    )

    sumilla = models.CharField(
        max_length=300,
        default='',
        blank=True,
        null=False
    )

    fecha_publicacion = models.DateTimeField(
        auto_now_add=True,
        # auto_now=True
        blank=True,
        null=False
    )

    contenido = models.TextField(
        blank=False,
        null=False
    )

    autor = models.ForeignKey(
        User,
        blank=False,
        null=False
    )
    # autor = models.OneToOneField(User)
    # autor = models.ManyToManyField(User)

    categoria = models.ForeignKey(Categoria)

    imagen = models.ImageField(
        upload_to='imagenes',
        blank=True,
        null=True
    )

    def __str__(self):
        return self.titular


class Comentario(models.Model):
    usuario = models.ForeignKey(User)

    noticia = models.ForeignKey(Noticia)

    texto = models.TextField(
        blank=False,
        null=False
    )

    fecha_publicacion = models.DateTimeField(
        auto_now_add=True
    )
