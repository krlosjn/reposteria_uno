from django.db import models
from apps.clientes.models import Clientes
from apps.postres.models import Postres

iva = [
    (0, 0),
    (19, 19),
]

# Create your models here.
class Pedidos(models.Model):
    clientes=models.ForeignKey(Clientes, null=True, blank=True, on_delete=models.CASCADE)
    fechapedido=models.DateField()
    fechaentrega=models.DateField()
    fechaenvio=models.DateField()
    formaenvio=models.CharField(max_length=50)
    destinatario=models.CharField(max_length=70)
    direcciondestinatario=models.TextField()
    ciudaddestinatario=models.CharField(max_length=70)


class DetallePedido(models.Model):
    postre=models.ForeignKey(Postres, null=True, blank=True, on_delete=models.CASCADE)
    pedido=models.ForeignKey(Pedidos, null=True, blank=True, on_delete=models.CASCADE)
    iva=models.IntegerField(null=True, blank=True, choices=iva,default=19)
    cantidad=models.IntegerField(null=True, blank=True)
    descuento=models.IntegerField(null=True, blank=True)
    subtotal=models.FloatField(null=True, blank=True)
    total=models.FloatField(null=True, blank=True)