# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-26 21:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pedido',
            name='estado',
        ),
        migrations.AddField(
            model_name='pedido',
            name='producto',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='pedidos.Producto', verbose_name='producto'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='EstadoPedido',
        ),
    ]
