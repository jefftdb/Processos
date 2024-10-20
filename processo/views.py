from django.shortcuts import render,get_object_or_404,redirect
from processo.forms import ProcessoForms
from django.views.decorators.csrf import csrf_protect
from processo.models import Processo

@csrf_protect
def novo_processo(request):
    if request.method == 'POST':
        form = ProcessoForms(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            print("Formulário salvo com sucesso")
            return render(request, 'index.html', {'mensagem': 'Processo cadastrado com sucesso!' })
        else:
            print("Formulário inválido")
            print(form.errors)
    else:
        form = ProcessoForms()
    return render(request, 'adicionar.html', {'form': form, 'titulo':'Processo'})

def exibir_processo(request,id):
    dados = Processo.objects.get(id=id)
    return render(request, 'exibir.html', {'dados' : dados,'titulo': dados.first_name,'aplicativo':'processo'})

def deletar_processo(request, id):
    processo = Processo.objects.get(id=id)
    titulo = processo.nome  
    funcionario.delete()  
    return render(request, 'exibir.html', {'mensagem': 'Processo ' + titulo + ' deletado com sucesso!' })

def alterar_processo(request,id):
    processo = get_object_or_404(Processo, id=id)
    if request.method == 'POST':
        form = ProcessoForms(request.POST, request.FILES, instance=processo) 
        if form.is_valid():
            form.save()  
            return redirect('Processo:exibir_processo', id=id)  
    else:
        form = ProcessoForms(instance=processo)  

    # Renderiza a página com o formulário
    return render(request, 'alterar.html', {'form': form})

def todos_processos(request):
    processos = Processo.objects.all()

    return render(request, 'todos.html',{'dados' : processos, 'titulo':'Todos os Processos'})
