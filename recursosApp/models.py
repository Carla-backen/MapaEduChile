from django.db import models

class RecursoEducativo(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=300)
    region = models.CharField(max_length=100)
    comuna = models.CharField(max_length=100)
    categoria = models.CharField(max_length=100)
    gratuito = models.BooleanField(default= True)
                              
    def __str__(self):
        return self.nombre