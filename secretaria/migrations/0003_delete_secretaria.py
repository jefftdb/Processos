# Generated by Django 5.1.2 on 2024-10-19 16:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('funcionario', '0006_delete_funcionario'),
        ('secretaria', '0002_remove_secretaria_endereco'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Secretaria',
        ),
    ]
