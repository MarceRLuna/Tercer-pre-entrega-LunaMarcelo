from django.db import models

# Create your models here.

class Inmueble(models.Model):
    
    #definimos los atributos que tendrá la clase

    categoria = models.CharField(max_length=30)
    ubicacion = models.CharField(max_length=50)
    domitorios = models.IntegerField()
    metros_cuadrados = models.IntegerField()

class Propietario(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    telefono = models.IntegerField()
    mail = models.EmailField()

class Inquilino(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    telefono = models.IntegerField()
    mail = models.EmailField()
    valor_alquiler = models.IntegerField()


