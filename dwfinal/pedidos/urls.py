from django.conf.urls import url
from pedidos import views

urlpatterns = [
    url(r'^nuevopedido/$', views.nuevo_pedido_view, name='nuevo_pedido'),
]
