from django.contrib import admin
from .models import Panel

class PanelAdmin(admin.ModelAdmin):
    model=Panel
    list_display = ['panel_nombre','panel_descripcion','panel_data_inicio','concluido']
    search_fields = ['panel_name']
    save_on_top = False
admin.site.register(Panel, PanelAdmin)


