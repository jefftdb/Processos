from django.shortcuts import render
from processo.forms import ProcessoForms
from django.views.decorators.csrf import csrf_protect

@csrf_protect
def novo_processo(request):
    if request.method == 'POST':
        form = ProcessoForms(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            print("Formulário salvo com sucesso")
            return redirect('index.html')
        else:
            print("Formulário inválido")
            print(form.errors)
    else:
        form = ProcessoForms()
    return render(request, 'adicionar.html', {'form': form, 'titulo':'Processo'})
