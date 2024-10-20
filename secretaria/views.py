from django.shortcuts import render
from secretaria.forms import SecretariaForms
from django.views.decorators.csrf import csrf_protect

@csrf_protect
def nova_secretaria(request):
    if request.method == 'POST':
        form = SecretariaForms(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            print("Formulário salvo com sucesso")
            return render(request, 'index.html', {'mensagem': 'Secretaria cadastrada com sucesso!' })
        else:
            print("Formulário inválido")
            print(form.errors)
    else:
        form = SecretariaForms()
    return render(request, 'adicionar.html', {'form': form, 'titulo':'Secretaria'})
