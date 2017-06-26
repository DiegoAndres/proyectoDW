from django import forms
from .models import Pedido


class PedidoForm ( forms.ModelForm ):
    """
        Formulario de Cliente
    """

    # nombre            = forms.CharField( required = True, label = "Nombre", widget = forms.TextInput( attrs = {"class" : "form-control"} ) )

    class Meta:
        model  = Pedido
        fields = '__all__'
