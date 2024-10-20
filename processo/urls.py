from django.urls import path
from . import views

app_name = 'Processo'

urlpatterns = [
    path('novo_processo', views.novo_processo, name="novo_processo"),

]