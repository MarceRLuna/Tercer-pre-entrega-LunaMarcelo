
from django.urls import path
# desde el archivo views en la carpeta de la aplicación importamos todas las funciones que ejecutaremos al ingresar a las urls
from app.views import inicio, lista_inmuebles, inmueble_formulario, inquilino_formulario, propietario_formulario, busqueda_inmueble, buscar 

urlpatterns = [
    path('', inicio, name="inicio"),    
    path('lista-inmuebles/', lista_inmuebles, name='buscar'),
    path('inmueble-formulario/', inmueble_formulario, name='inmueble_formulario'),
    path('inquilino-formulario/', inquilino_formulario, name='inquilino_formulario'),
    path('propietario-formulario/', propietario_formulario, name='propietario_formulario'),
    path('busqueda-inmueble/', busqueda_inmueble, name='busqueda_inmueble'), # endpoint que denominamos "busqueda-inmueble/" que invoca a la función "busqueda_inmueble"
    path('buscar/', buscar, name='buscar_inmueble') # endpoint que tiene la función "buscar" y que se invoca cuando el formulario del template "busqueda_inmueble.html" se submitea.
]
