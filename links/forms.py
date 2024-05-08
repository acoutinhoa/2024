from django import forms
from .models import Ps, Tg

class ProjetoForm(forms.ModelForm):
    class Meta:
        model = Tg
        fields = ('tag', )

class ProjetoForm(forms.ModelForm):
    class Meta:
        model = Ps
        fields = ('visivel', 'imagem', 'titulo', 'link', 'ativo', 'link2' 'obs', 'tags', )
