from django.urls import path
from . import views

app_name = 'Secretaria'

urlpatterns = [
    path('nova_secretaria', views.nova_secretaria, name="nova_secretaria"),

]