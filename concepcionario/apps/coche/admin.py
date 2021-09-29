from django.contrib import admin
from django.db.models.query_utils import RegisterLookupMixin
from apps.coche.models import Coche

class CocheAdmin(admin.ModelAdmin):
    list_display = ('matricula', 'modelo', 'codigo_m', 'color', 'precio')
# Register your models here.

admin.site.register(Coche, CocheAdmin)

