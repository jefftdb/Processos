from django import forms
from .models import Endereco

class EnderecoForms(forms.ModelForm):
    class Meta:
        model = Endereco
        fields = ['rua','numero','cidade','estado', 'cep',  'bairro','pais']

        widgets = {
            'País   :': forms.TextInput(attrs={'class': 'form-control'}),
            'Estado :': forms.TextInput(attrs={'class': 'form-control'}),
            'cep    :': forms.TextInput(attrs={'class': 'form-control'}),
            'Cidade :': forms.TextInput(attrs={'class': 'form-control'}),
            'Bairro :': forms.TextInput(attrs={'class': 'form-control'}),
            'Rua    :': forms.TextInput(attrs={'class': 'form-control'}),
            'Número :': forms.TextInput(attrs={'class': 'form-control'}),

        }

