from django.db import models

# Create your models here.
class Clientes(models.Model):
    idClientes=models.CharField(max_length=50)
    nombre=models.CharField(max_length=50)
    apellidos=models.CharField(max_length=70)
    direccion=models.TextField()
    ciudad=models.CharField(max_length=50)
    telefono=models.IntegerField()
    email=models.EmailField()

    def __str__(self):
        return '{} {}'.format(self.nombre, self.apellidos)