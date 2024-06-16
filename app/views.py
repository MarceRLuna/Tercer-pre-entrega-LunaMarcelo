from django.http import HttpResponse 
from django.shortcuts import render
from .models import Inmueble, Propietario, Inquilino  # importamos los modelos que utilizaremos en las funciones
from .forms import Inmueble_Formulario, Inquilino_Formulario, Propietario_Formulario

# Create your views here.

def inicio(req):
    return render(req, "inicio.html", {})


def inmueble_formulario(req):

    if req.method == 'POST':
        
        mi_formulario_inmueble = Inmueble_Formulario(req.POST)

        if mi_formulario_inmueble.is_valid():

            data = mi_formulario_inmueble.cleaned_data

            # creamos una instancia de la clase Inmueble.
            nuevo_inmueble = Inmueble(categoria=data['categoria'], ubicacion=data['ubicacion'], domitorios=data['domitorios'], metros_cuadrados=data['metros_cuadrados']) 
    
            nuevo_inmueble.save() # con el método .save() guardamos en la base de datos la instancia que creamos.

            return render(req, "inicio.html", {"message": "Inmueble creado con éxito"})
        
        else:
            return render(req, "inicio.html", {"message": "Datos inválidos"})
    else:
        mi_formulario_inmueble = Inmueble_Formulario()

        return render(req, "inmueble_formulario.html", {"mi_formulario_inmueble": mi_formulario_inmueble})
    



def inquilino_formulario(req):
    
    # si se invoca a la función inquilino_formulario con una solicitud de tipo POST, significa que se clickeo el botón para enviar la información cargada al formulario y se ejecuta el código del if

    if req.method == 'POST':
        
        mi_formulario_inquilino = Inquilino_Formulario(req.POST) # almaceno en una variable todos los datos que se cargan en el formulario

        if mi_formulario_inquilino.is_valid(): # Utilizamos el método is_valid que tienen todos los formularios creados con la clase de Django From para validar los datos ingresados al formulario

            data = mi_formulario_inquilino.cleaned_data # Recuperamos los datos ya validados del formulario y los guardamos en la variable "data"

            # utilizamos la variable "data" para crear una instancia de la clase Inquilino
            nuevo_inquilino = Inquilino(nombre=data['nombre'], apellido=data['apellido'], telefono=data['telefono'], mail=data['mail'], valor_alquiler=data['valor_alquiler'])

            nuevo_inquilino.save() # guardamos dicha instancia en nuestra base de datos con el método .save()

            return render(req, "inicio.html", {"message": "Datos del inquilino cargados con éxito"}) # retornamos al usuario a la página de inicio e imprimimos el mensaje almacenado en el contexto
        
        else:
            return render(req, "inicio.html", {"message": "Datos inválidos"})
    
    else:
        # se ejecuta el siguiente código cuando se invoca a la función inquilino_formulario al ingresar a la url, es decir con la solicitud de tipo GET

        mi_formulario_inquilino = Inquilino_Formulario()

        return render(req, "inquilino_formulario.html", {"mi_formulario_inquilino": mi_formulario_inquilino})
    



def propietario_formulario(req):

    
    if req.method == 'POST':

        mi_formulario_propietario = Propietario_Formulario(req.POST)

        if mi_formulario_propietario.is_valid():

            data = mi_formulario_propietario.cleaned_data
        
            nuevo_propietario = Propietario(nombre=data['nombre'], apellido=data['apellido'], telefono=data['telefono'], mail=data['mail'])

            nuevo_propietario.save() 

            return render(req, "inicio.html", {"message": "Datos del propietario cargados con éxito"})
        
        else:
            return render(req, "inicio.html", {"message": "Datos inválidos"})
    
    else:
        mi_formulario_propietario = Propietario_Formulario()

        return render(req, "propietario_formulario.html", {"mi_formulario_propietario": mi_formulario_propietario})


# función que busca todas los datos guardados en la base de datos del modelo Inmueble
def lista_inmuebles(req):
    
    lista = Inmueble.objects.all() # manager que me permite recuperar todos los datos almacenados en la tabla Inmueble, creada en la base de datos. En la variable "lista" guardamos la info.
    
    return render(req, "lista_inmuebles.html", {"lista_inmuebles" : lista}) 


def busqueda_inmueble(req): # esta función solo renderiza un html que se llama "busqueda_inmueble.html"

    return render(req, "busqueda_inmueble.html", {})



def buscar(req):

    if req.GET["domitorios"]:

        domitorios = req.GET["domitorios"]

        inmueble = Inmueble.objects.filter(domitorios = domitorios) #guardamos en la variable "inmueble" al inmueble que coincida con el criterio de busqueda definido entre los paréntesis (), es decir, recupera el inmueble cuya cantidad de dormitorios sea igual a la cantidad de dormitorios que ingresa el usuario

        return render(req, "resultado_busqueda.html", {"inmueble": inmueble, "domitorios": domitorios})

    else:
        return render(req, "inicio.html", {"message": "Datos inválidos"})