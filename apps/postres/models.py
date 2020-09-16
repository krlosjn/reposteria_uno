from django.db import models
from django.utils import timezone

postres_estado = [
    (1, 'Activo'),
    (2, 'Inactivo')
]

# Crear la clase con sus atributos (se asemeja en la base de datos a la tabla con sus campos).
class Postres(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.FloatField()
    stock = models.IntegerField()
    img =  models.FileField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    Estado = models.IntegerField(null=False, blank=False, choices = postres_estado, default=1)

    def __str__(self):
        return '{} {}'.format(self.nombre, self.precio)
    
class Meta:
    db_table = 'postres'