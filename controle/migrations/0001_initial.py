# Generated by Django 5.2 on 2025-04-21 01:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('telefone', models.TextField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Conta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_vencimento', models.DateTimeField()),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='controle.cliente')),
            ],
        ),
        migrations.CreateModel(
            name='PontoDeAcesso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=20)),
                ('data_instalacao', models.DateTimeField()),
                ('data_cancelamento', models.DateTimeField(null=True)),
                ('endereco', models.TextField()),
                ('plano', models.CharField(choices=[('10', '10 megas'), ('10F', '10 Megas Fibre'), ('100', '100 Megas'), ('100F', '100 Megas Fibra'), ('500', '500 Megas'), ('500F', '500 Megas Fibra')], default=10, max_length=4)),
                ('ativo', models.BooleanField(default=True)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='controle.cliente')),
            ],
        ),
    ]
