from django import forms
from .models import *

class ProjetoForm(forms.ModelForm):
    class Meta:
        model = Projeto
        fields = ('visivel', 'titulo', 'texto', 'tags', )
