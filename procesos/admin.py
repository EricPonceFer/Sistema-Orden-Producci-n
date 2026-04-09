
from django.contrib import admin
from .models import Plantilla, Paso

class PasoInline(admin.TabularInline):
    model = Paso
    extra = 1

@admin.register(Plantilla)
class PlantillaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'fecha_creacion')
    inlines = [PasoInline]