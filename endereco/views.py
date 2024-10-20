from django.shortcuts import render
from endereco.forms import EnderecoForms
from django.views.decorators.csrf import csrf_protect

@csrf_protect
def novo_endereco(request):
    if request.method == 'POST':
        form = EnderecoForms(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            print("Formulário salvo com sucesso")
            return render(request, 'index.html', {'mensagem': 'Endereço cadastrado com sucesso!' })
        else:
            print("Formulário inválido")
            print(form.errors)
    else:
        form = EnderecoForms()
    return render(request, 'adicionar.html', {'form': form, 'titulo':'Endereço'})
