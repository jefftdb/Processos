# Generated by Django 5.1.2 on 2024-10-19 16:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('funcionario', '0005_remove_funcionario_endereco'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Funcionario',
        ),
    ]
