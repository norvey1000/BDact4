from apps import marca
from django.contrib import admin
from django.db.models.query_utils import RegisterLookupMixin

from apps.marca.models import Marca

class MarcaAdmin(admin.ModelAdmin):
    list_display = ('codigo_m', 'descripcion')
# Register your models here.

admin.site.register(Marca, MarcaAdmin)







