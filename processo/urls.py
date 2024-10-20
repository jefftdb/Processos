from django.urls import path
from . import views

app_name = 'Processo'

urlpatterns = [
    path('novo_processo', views.novo_processo, name="novo_processo"),
    path('exibir_processo/<int:id>/', views.exibir_processo,name = "exibir_processo"),
    path('deletar_processo/<int:id>', views.deletar_processo,name = "deletar_processo"),
    path('alterar_processo/<int:id>', views.alterar_processo,name = "alterar_processo"),
    path('todos_processos/', views.todos_processos,name = "todos_processos")

]