# Generated by Django 5.1.2 on 2024-10-19 16:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('funcionario', '0004_funcionario_endereco_alter_funcionario_processos_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='funcionario',
            name='endereco',
        ),
    ]
