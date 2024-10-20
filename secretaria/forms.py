from django import forms
from .models import Secretaria

class SecretariaForms(forms.ModelForm):
    class Meta:
        model = Secretaria
        fields = ['nome','endereco']

        widgets = {
            'Nome    :': forms.TextInput(attrs={'class': 'form-control'}),
            'Endereço:': forms.SelectMultiple(attrs={'class': 'form-control'}),

        }
