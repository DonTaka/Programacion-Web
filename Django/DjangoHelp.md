Pasos de instalacion y creacion de proyecto con django <br>
1.- Revisar instalaciones de python (py y pip) <br>
2.- instalar django con comando pip install django <br>
3.- revisar que el comando django-admin funcione <br>
4.- levantar el entorno de django <br>
5.- ingresar a la carpeta por medio del comando cd nombreCarpeta <br>
6.- crear pagina django <br>
7.- agregar app al apartado installed_apps del archivo settings.py <br>
8.- agregar el enrutamiento urls del proyecto al archivo urls.py de Django <br>
9.- realizar la migracion en proyecto creado <br>

Notas

Comandos de validacion de version e instalacion <br>
py --version <br>
pip --version <br>
django-admin --version

Comando para montar entorno de django <br>
django-admin startproject nombreEntorno

Comando para crear pagina u aplicacion de Django <br>
py manage.py startapp nombrePagina||nombreAplicacion

settings.py = archivo de configuraciones <br>
urls.py = configuracion de rutas de django

Etiquetas de html de django <br>
{% load static %} = permite cargar los recursos de static en la pagina que  
 se desee utilizarlos <br>
{% static %} = referencia la ruta static de django <br>
{% url %} = referencia el archivo de enrutamientos del proyecto urls.py <br>
{{ variable }} = referencia variable entregada por el context <br>
