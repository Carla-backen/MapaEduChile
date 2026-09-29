from django.db import models


class Region(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Comuna(models.Model):
    nombre = models.CharField(max_length=100)
    region = models.ForeignKey(
        Region,
        on_delete=models.CASCADE,
        related_name='comunas'
    )

    def __str__(self):
        return self.nombre


class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(
        max_length=200,
        blank=True
    )

    def __str__(self):
        return self.nombre


class RecursoEducativo(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=300)

    comuna = models.ForeignKey(
        Comuna,
        on_delete=models.CASCADE,
        related_name='recursos'
    )

    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.CASCADE,
        related_name='recursos'
    )

    direccion = models.CharField(
        max_length=200,
        blank=True
    )

    latitud = models.DecimalField(
        max_digits=9,
        decimal_places=6,
        null=True,
        blank=True
    )

    longitud = models.DecimalField(
        max_digits=9,
        decimal_places=6,
        null=True,
        blank=True
    )

    sitio_web = models.URLField(
        blank=True
    )

    gratuito = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre