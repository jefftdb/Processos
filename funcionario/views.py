from django.shortcuts import render
from funcionario.forms import FuncionarioForms
from django.views.decorators.csrf import csrf_protect
from funcionario.models import Funcionario

@csrf_protect
def novo_funcionario(request):
    if request.method == 'POST':
        form = FuncionarioForms(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            print("Formulário salvo com sucesso")
            return redirect('index.html')
        else:
            print("Formulário inválido")
            print(form.errors)
    else:
        form = FuncionarioForms()
    return render(request, 'adicionar.html', {'form': form, 'titulo':'Funcionário'})

def exibir_funcionario(request,id):
    dados = Funcionario.objects.get(id=id)
    return render(request, 'exibir.html', {'dados' : dados,'titulo': dados.first_name})

def deletar_funcionario(request, id):
    funcionario = Funcionario.objects.get(id=id)
    titulo = funcionario.first_name +" " +funcionario.last_name  
    funcionario.delete()  
    return render(request, 'exibir.html', {'mensagem': 'Usuario ' + titulo + ' deletado com sucesso!' })
