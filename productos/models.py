from django.db import models
from django.utils import timezone


class Producto(models.Model):

    nombre:str = models.CharField(max_length=200,
                                  blank=False, null=False)
    descripcion:str = models.TextField(blank=False, null=False)
    precio:float = models.PositiveIntegerField(default=0, null=False)
    fecha_registro = models.DateField (default=timezone.now())
    estatus:bool = models.BooleanField(default=True)