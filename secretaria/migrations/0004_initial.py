# Generated by Django 5.1.2 on 2024-10-19 16:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('endereco', '0006_initial'),
        ('secretaria', '0003_delete_secretaria'),
    ]

    operations = [
        migrations.CreateModel(
            name='Secretaria',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=45)),
                ('endereco', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='endereco_secretaria', to='endereco.endereco')),
            ],
        ),
    ]
