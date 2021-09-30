from django.db.models.deletion import CASCADE
from django.db import models
from apps.cliente.models import Cliente
from apps.coche.models import Coche


# Create your models here.

class Venta(models.Model):
    CLIENTE = models.ForeignKey(Cliente, verbose_name="CLIENTE", null=True, blank=True, on_delete=CASCADE)
    VEHICULO = models.ForeignKey(Coche, null=True, blank=True, on_delete=CASCADE)
    fecha = models.DateField(verbose_name='fecha de venta')
    total = models.IntegerField()
    


