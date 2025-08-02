from django import forms
from .models import Proyecto, Habilidad


class ProyectoForm(forms.ModelForm):
    class Meta:
        model = Proyecto
        fields = ['titulo', 'descripction', 'fecha', 'url']


class HabilidadForm(forms.ModelForm):
    class Meta:
        model = Habilidad
        fields = ['nombre', 'nivel']