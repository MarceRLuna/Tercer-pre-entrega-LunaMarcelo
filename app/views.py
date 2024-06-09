from django.http import HttpResponse 
from django.shortcuts import render
from .models import Inmueble, Propietario, Inquilino  # importamos los modelos que utilizaremos en las funciones

# Create your views here.

def inicio(req):
    return render(req, "inicio.html", {})


# función que crea nuevas propiedades
def inmueble (req):
    
    # nuevo_inmueble = Inmueble() # creamos una instancia de la clase Inmueble.
    
    # nuevo_inmueble.save() # con el método .save() guardamos en la base de datos la instancia que creamos. 
    return render(req, "inmueble.html", {})

# función que busca todas los datos guardados en la base de datos del modelo Inmueble
def lista_inmuebles(req):
    
    lista = Inmueble.objects.all() # manager que me permite recuperar todos los datos almacenados en la tabla Inmueble, creada en la base de datos. En la variable "lista" guardamos la info.
    
    return render(req, "lista_inmuebles.html", {"lista_inmuebles" : lista}) 


def propietario (req):
    
    # nuevo_propietario = Propietario() 
    
    # nuevo_propietario.save()

    return render(req, "propietario.html", {})


def inquilino (req):
    
    # nuevo_inquilino = Inquilino() 
    
    # nuevo_inquilino.save()

    return render(req, "inquilino.html", {})   