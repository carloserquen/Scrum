from django import forms

from .models import Panel
class PanelForm(forms.ModelForm):
    class Meta:
        model = Panel
        fields = ('panel_nombre','panel_descripcion')