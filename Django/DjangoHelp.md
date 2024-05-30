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
py --version : Validar version del python(y que funcione) <br>
pip --version : Validar version del PIP (y que funcione) <br>
django-admin --version : Validar version de Django( y que funcione)<br>

Comando para montar entorno de django <br>
django-admin startproject nombreEntorno

Comando para crear aplicacion de Django <br>
py manage.py startapp nombrePagina||nombreAplicacion

settings.py = archivo de configuraciones <br>
urls.py = configuracion de rutas de django <br>
models.py = archivo encargado de generar y gestionar modelos de datos creados con Django <br>
admin.py = archivo encargado de gestionar los modelos que estan registrados en el panel administrativo de Django

Enlaces de interes <br>

Informacion models : https://docs.djangoproject.com/en/5.0/topics/db/models/ <br>
Informacion Fields del models: https://docs.djangoproject.com/en/5.0/ref/models/fields/ <br>

Etiquetas de html de django <br>
{% load static %} = permite cargar los recursos de static en la pagina que  
 se desee utilizarlos <br>
{% static %} = referencia la ruta static de django <br>
{% url %} = referencia el archivo de enrutamientos del proyecto urls.py <br>
{{ variable }} = referencia variable entregada por el context <br>
