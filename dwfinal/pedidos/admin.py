# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Producto, Pedido


admin.site.register(Pedido)
admin.site.register(Producto)
