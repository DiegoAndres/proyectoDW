# -*- coding: utf-8 -*-
from django.db import models
from clientes.models import Cliente


class Producto(models.Model):
    """
        Modelo Producto
    """
    nombre          = models.CharField( max_length = 70, verbose_name = u'nombre', help_text = "Nombre Producto" )
    descripcion     = models.CharField( blank = True, null = True, max_length = 100, verbose_name = u'descripcion', help_text = "Descripcion Producto" )
    valor           = models.IntegerField( verbose_name = u'valor', help_text = "Valor del Producto" )
    activo          = models.BooleanField( default = True)
    fecha_creacion  = models.DateTimeField( auto_now_add = True )

    def __unicode__( self ):
        return self.nombre


class Pedido(models.Model):
    """
        Modelo Pedido
    """
    cliente            = models.ForeignKey( Cliente, verbose_name = u'cliente' )
    boleta             = models.IntegerField( verbose_name = u'boleta', help_text = "Numero de Boleta" )
    producto           = models.ForeignKey( Producto, verbose_name = u'producto')
    fecha_creacion     = models.DateTimeField( auto_now_add = True )
    fecha_modificacion = models.DateTimeField( auto_now = True )

    def __unicode__( self ):
        return self.nombre
