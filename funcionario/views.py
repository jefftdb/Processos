from django.shortcuts import render
from funcionario.forms import FuncionarioForms
from django.views.decorators.csrf import csrf_protect

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
