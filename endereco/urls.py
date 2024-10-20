from django.urls import path
from . import views

app_name = 'Endereco'

urlpatterns = [
    path('novo_endereco', views.novo_endereco, name="novo_endereco"),

]