# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import PedidoForm
from .models import Pedido


@login_required
def nuevo_pedido_view(request):
    if request.POST:
        form = PedidoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success( request, 'Pedido creado correctamente.' )
    pedidos = Pedido.objects.all()
    form = PedidoForm()
    return render(request, 'pedidos/nuevo_pedido.html', {
        'form'   : form,
        'pedidos': pedidos,
        })
