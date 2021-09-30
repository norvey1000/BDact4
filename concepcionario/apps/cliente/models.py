from django.db import models

# Create your models here.

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=50)
    ciudad = models.CharField(max_length=100)
    telefono = models.CharField(null=True, blank=True, max_length=20)


