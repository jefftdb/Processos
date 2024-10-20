from django.urls import path
from . import views

app_name = 'Funcionario'

urlpatterns = [
    path('novo_funcionario', views.novo_funcionario, name="novo_funcionario"),
    path('exibir_funcionario/<int:id>', views.exibir_funcionario,name = "exibir_funcionario"),
    path('deletar_funcionario/<int:id>', views.deletar_funcionario,name = "deletar_funcionario")


]