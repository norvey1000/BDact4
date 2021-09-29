from django.contrib import admin
from django.db.models.query_utils import RegisterLookupMixin
from apps.cliente.models import Cliente

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'direccion', 'ciudad', 'telefono')
# Register your models here.

admin.site.register(Cliente, ClienteAdmin)

