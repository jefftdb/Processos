from django.urls import path
from . import views

app_name = 'Funcionario'

urlpatterns = [
    path('novo_funcionario', views.novo_funcionario, name="novo_funcionario"),

]