from django import forms
from .models import Funcionario

class FuncionarioForms(forms.ModelForm):
    class Meta:
        model = Funcionario
        fields = ['foto','username','password','first_name','last_name','email','cpf', 'telefone', 'data_nascimento', 'secretarias', 'processos', 'endereco']

        widgets = {            
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite seu nome'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite seu sobrenome'}),
            'cpf': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite o CPF'}),
            'telefone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite o Telefone'}),
            'email' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite seu email', 'type':'email'}),
            'data_nascimento': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Selecione a Data', 'type': 'date'}),
            'secretarias': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'processos': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'endereco': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite um usuário'}),
            'password':forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Digite sua senha'})
        }
