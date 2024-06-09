
from django.urls import path
# desde el archivo views en la carpeta de la aplicación importamos todas las funciones que ejecutaremos al ingresar a las urls
from app.views import inicio, inmueble, propietario, inquilino, lista_inmuebles, inmueble_formulario 

urlpatterns = [
    path('', inicio, name="inicio"),
    path('inmueble/', inmueble, name="inmueble"), #enlace que me permite ejecutar la función "inmueble"
    path('propietario/', propietario, name= 'propietario'),
    path('inquilino/', inquilino, name='inquilino'),
    path('lista-inmuebles/', lista_inmuebles, name='buscar'),
    path('inmueble-formulario/', inmueble_formulario, name='inmueble_formulario'),
]
