from django.db import models

# Create your models here.

class Cliente(models.Model):
    nit_c = models.CharField(verbose_name='n° de identificacion', null= True, max_length=20)
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=50)
    ciudad = models.CharField(max_length=100)
    telefono = models.CharField(null=True, blank=True, max_length=20)

def __str__(self):
        texto = "{0},{1},{2},{3},{4}"
        return texto.format(self.nit_c, self.nombre, self.direccion, self.ciudad, self.telefono)

        
def __str__(self):
        texto = "{0}"
        return texto.format(self.nit_c)
