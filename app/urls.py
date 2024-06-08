
from django.urls import path
# desde el archivo views en la carpeta de la aplicación importamos todas las funciones que ejecutaremos al ingresar a las urls
from app.views import inicio, inmueble, propietario, inquilino, lista_inmuebles 

urlpatterns = [
    path('', inicio),
    path('inmueble/', inmueble), #enlace que me permite ejecutar la función "inmueble"
    path('propietario/', propietario),
    path('inquilino/', inquilino),
    path('lista-inmuebles/', lista_inmuebles),
]
