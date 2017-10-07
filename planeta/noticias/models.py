from django.db import models


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

    def __str__(self):
        return self.titular

    # autor =
    # categoria =
