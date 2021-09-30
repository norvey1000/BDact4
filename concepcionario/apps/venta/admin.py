from django.contrib import admin
from django.db.models.query_utils import RegisterLookupMixin


from apps.venta.models import Venta

class VentaAdmin(admin.ModelAdmin):
    list_display = ('CLIENTE', 'VEHICULO', 'fecha', 'total')
# Register your models here.

admin.site.register(Venta, VentaAdmin)


