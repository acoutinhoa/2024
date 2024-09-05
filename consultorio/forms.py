from django import forms
from .models import *

class NomeForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = ['nome',]

class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = ['nome','cpf', 'nascimento', 'obs',]
        widgets = {
            'obs': forms.Textarea(attrs={'rows': 1}),
            # 'tags' : forms.CheckboxSelectMultiple(attrs={'class': 'form_tags'}),
            }

ContatoFormSet = forms.inlineformset_factory(
    Paciente,
    Contato,
    exclude = ['paciente'],
    extra = 0,
    # can_delete = False,
    widgets = {
        'obs': forms.Textarea(attrs={'rows': 1}),
        # 'tipo' : forms.RadioSelect(attrs={'class': 'form_tags'}),
        },
    # label_suffix = "????",
    )

EnderecoFormSet = forms.inlineformset_factory(
    Paciente,
    Endereco,
    exclude = ['paciente'],
    max_num= 1,
    can_delete = False,
    widgets = {
        'rua': forms.Textarea(attrs={'rows': 1}),
        },
    # label_suffix = "????",
    )

