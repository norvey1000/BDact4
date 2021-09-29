from django.db import models
# from apps.marca.models import Marca

# Create your models here.
class Marca(models.Model):
    codigo_m = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=400)
    
  
