from django.shortcuts import render,get_object_or_404,redirect
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
            return render(request, 'index.html', {'mensagem': 'Usuario cadastrado com sucesso!' })
        else:
            print("Formulário inválido")
            print(form.errors)
    else:
        form = FuncionarioForms()
    return render(request, 'adicionar.html', {'form': form, 'titulo':'Funcionário'})

def exibir_funcionario(request,id):
    dados = Funcionario.objects.get(id=id)
    return render(request, 'exibir.html', {'dados' : dados,'titulo': dados.first_name,'aplicativo':'funcionario'})

def deletar_funcionario(request, id):
    funcionario = Funcionario.objects.get(id=id)
    titulo = funcionario.first_name +" " +funcionario.last_name  
    funcionario.delete()  
    return render(request, 'exibir.html', {'mensagem': 'Usuario ' + titulo + ' deletado com sucesso!' })

def alterar_funcionario(request,id):
    funcionario = get_object_or_404(Funcionario, id=id)
    if request.method == 'POST':
        form = FuncionarioForms(request.POST, request.FILES, instance=funcionario) 
        if form.is_valid():
            form.save()  
            return redirect('Funcionario:exibir_funcionario', id=id)  
    else:
        form = FuncionarioForms(instance=funcionario)  

    # Renderiza a página com o formulário
    return render(request, 'alterar.html', {'form': form})

def todos_funcionarios(request):
    funcionarios = Funcionario.objects.all()

    return render(request, 'todos.html',{'dados' : funcionarios, 'titulo':'Todos os Funcionários'})
