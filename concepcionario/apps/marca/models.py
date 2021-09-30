from django.db import models
# from apps.marca.models import Marca

# Create your models here.
class Marca(models.Model):
    codigo_m = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=400)

    def __str__(self):
        texto = "{0},{1}"
        return texto.format(self.codigo_m, self.descripcion)
    
  
