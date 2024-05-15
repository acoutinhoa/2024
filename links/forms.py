from django import forms
from .models import Ps, Tg

class TgForm(forms.ModelForm):
    class Meta:
        model = Tg
        fields = ('tag', )

PsAddForm = forms.modelform_factory(
    Ps,
    fields = ('imagem',),
    )

PsForm = forms.modelform_factory(
    Ps,
    fields = ('imagem', 'titulo', 'link', 'ativo', 'link2','obs','tags'),
    widgets = {
        'obs': forms.Textarea(attrs={'rows': 5}),
        # 'tags' : forms.CheckboxSelectMultiple(),
        'tags' : forms.CheckboxSelectMultiple(attrs={'class': 'form_tags'}),
        },
    )
