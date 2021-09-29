from django.db import models
from django.db.models.deletion import CASCADE
# from apps.coche.models import Coche
from apps.marca.models import Marca

# Create your models here.

class Coche(models.Model):
    matricula = models.CharField(max_length=10)
    modelo = models.CharField(max_length=100)
    codigo_m = models.ForeignKey(Marca, null=True, blank=True, on_delete=CASCADE)
    color = models.CharField(max_length=30)
    precio = models.DecimalField(max_digits=20, decimal_places=3)

    def __str__(self):
        texto = "{0},{1},{2},{3},{4}"
        return texto.format(self.matricula, self.modelo, self.codigo_m, self.color, self.precio)

    def __str__(self):
        texto = "{0}"
        return texto.format(self.codigo_m)

