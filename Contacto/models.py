from django.db import models
from django.forms import IntegerField


# Create your models here.

class Contactos(models.Model):
    nombre_apellido = models.CharField(max_length=50)
    id = models.BigIntegerField(primary_key=id)
    correo = models.EmailField(max_length=50)
    direccion = models.CharField(max_length=50)
    departamento = models.CharField(max_length=50)
    ciudad = models.CharField(max_length=50)
    celular = models.BigIntegerField()
    pagar = models.DecimalField(max_digits=10, decimal_places=3)
    producto_Comprado = models.CharField(max_length=50)
    
