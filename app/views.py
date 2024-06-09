from django.http import HttpResponse 
from django.shortcuts import render
from .models import Inmueble, Propietario, Inquilino  # importamos los modelos que utilizaremos en las funciones

# Create your views here.

def inicio(req):
    return render(req, "inicio.html", {})



# función que busca todas los datos guardados en la base de datos del modelo Inmueble
def lista_inmuebles(req):
    
    lista = Inmueble.objects.all() # manager que me permite recuperar todos los datos almacenados en la tabla Inmueble, creada en la base de datos. En la variable "lista" guardamos la info.
    
    return render(req, "lista_inmuebles.html", {"lista_inmuebles" : lista}) 


def inmueble_formulario(req):

    if req.method == 'POST':
        
        # creamos una instancia de la clase Inmueble.
        nuevo_inmueble = Inmueble(categoria=req.POST['categoria'], ubicacion=req.POST['ubicacion'], domitorios=req.POST['domitorios'], metros_cuadrados=req.POST['metros_cuadrados']) 
    
        nuevo_inmueble.save() # con el método .save() guardamos en la base de datos la instancia que creamos.

        return render(req, "inicio.html", {})
    
    else:
        return render(req, "inmueble_formulario.html", {})
    
def inquilino_formulario(req):

    if req.method == 'POST':
        
        nuevo_inquilino = Inquilino(nombre=req.POST['nombre'], apellido=req.POST['apellido'], telefono=req.POST['telefono'], mail=req.POST['mail'], valor_alquiler=req.POST['valor_alquiler'])

        nuevo_inquilino.save() 

        return render(req, "inicio.html", {})
    
    else:
        return render(req, "inquilino_formulario.html", {})
    

def propietario_formulario(req):

    if req.method == 'POST':
        
        nuevo_propietario = Propietario(nombre=req.POST['nombre'], apellido=req.POST['apellido'], telefono=req.POST['telefono'], mail=req.POST['mail'])

        nuevo_propietario.save() 

        return render(req, "inicio.html", {})
    
    else:
        return render(req, "propietario_formulario.html", {})        