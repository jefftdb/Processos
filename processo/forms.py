from django import forms
from .models import Processo

class ProcessoForms(forms.ModelForm):
    class Meta:
        model = Processo
        fields = ['numero','descricao']

        widgets = {
            'Número': forms.TextInput(attrs={'class': 'form-control'}),
            'Descrição': forms.TextInput(attrs={'class': 'form-control'}),

        }
