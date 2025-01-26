# Como correr una aplicacion Backend en Django

<br/><br/>

<h3>1. Introducción a Django</h3><hr/>

Django es un framework web de Python de alto nivel que facilita el desarrollo rápido de aplicaciones web. Se basa en el patrón de diseño Modelo-Vista-Controlador (MVC). Proporciona herramientas y funcionalidades preconstruidas para tareas comunes como:

    1. Manejo de bases de datos (ORM)
    2. Autenticación de usuarios
    3. Creación de formularios
    4. Manejo de URLs
    5. Administración de contenido

<br/><h3>2. Requisitos previos</h3><hr/>
Conocimientos básicos de Python: Familiaridad con variables, funciones, estructuras de control, etc.
Conocimientos básicos de <b>HTML, CSS y JavaScript</b>, para entender cómo se construyen las interfaces de usuario.

<br/><h3>3. Instalación</h3><hr/>

- Instalar Python 3.
- Instalar Django usando <code>pip install django</code>

<br/><h3>4. Creación de un proyecto Django</h3><hr/>

Utilizar el comando <code>django-admin startproject \<projectname\></code> para crear un nuevo proyecto Django.
Una vez que tienes un proyecto Django, puedes crear aplicaciones dentro de él para organizar tu código de manera lógica. Cada aplicación puede representar una funcionalidad específica de tu sitio web.

<br/>Comando: <code>python manage.py startapp \<appname\></code>

<br/><b>appname</b> Es el nombre que le das a tu aplicación. Puedes reemplazarlo por el nombre que quieras.

<br/><b>Estructura de la aplicación:</b> Django crea una nueva carpeta con el nombre de tu aplicación y dentro de ella genera varios archivos:

<b>models.py:</b> Aquí definirás los modelos de datos que representarán las entidades de tu aplicación (por ejemplo, usuarios, publicaciones, comentarios).

<b>views.py:</b> Contiene las vistas, que son las funciones que generan las respuestas HTTP a las solicitudes del usuario.

<b>urls.py:</b> Define las URLs de tu aplicación y cómo se mapean a las vistas.

<b>tests.py:</b> Aquí puedes escribir pruebas unitarias para tu aplicación.

<b>\_\_ init\_\_.py:</b> Un archivo vacío que indica a Python que esta carpeta es un paquete.

<br/><h3>5. Creación de una aplicación Django</h3><hr/>

Utilizar el comando <code>python manage.py startapp \<appname\></code> dentro del directorio del proyecto para crear una nueva aplicación. Django utiliza un ORM <b>(Object-Relational Mapper)</b> para interactuar con la base de datos. Esto significa que puedes definir tus modelos de datos como si fueran clases de <b>Python</b> y Django se encarga de traducirlos a consultas <b>SQL</b>.

Configuración en <b>settings.py:</b> Abre el archivo <b>settings.py</b> de tu proyecto.
Busca la sección DATABASES y configura la conexión a tu base de datos. Django soporta múltiples bases de datos, pero SQLite es una buena opción para empezar (no lo modifiques), este proyecto ya cuenta con una base de datos diferente, en el tuyo dejalo tal cual. Ejemplo:

```Python
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
```

<b>Creación de migraciones:</b>
Las migraciones son archivos que describen los cambios que se realizarán en la base de datos. Ejecuta el comando <code>python manage.py makemigrations</code> para crear las migraciones iniciales. Ejecuta el comando <code>python manage.py migrate</code> para aplicar las migraciones a la base de datos.

Ejemplo de un modelo:

```Python
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    body = models.TextField()
```

Este modelo define una tabla llamada Post con tres campos: title, pub_date y body.

¿Qué más puedes hacer con estos pasos?

- Crear vistas: Define funciones en <b>views.py</b> para manejar diferentes solicitudes HTTP (por ejemplo, mostrar una lista de publicaciones, mostrar una publicación individual, crear una nueva publicación).
- Crear plantillas: Crea archivos HTML en la carpeta templates para renderizar las vistas. Django utiliza un sistema de plantillas sencillo y poderoso para generar HTML dinámico.
- Definir URLs: Mapear las URLs de tu aplicación a las vistas correspondientes en el archivo <b>urls.py</b>.
- Crear formularios: Utilizar el sistema de formularios de Django para crear formularios web.

<br/><h3>6. Configuración de la base de datos</h3><hr/>

- Configurar la conexión a la base de datos en el archivo <b>settings.py</b> del proyecto. Yo configure ya la BDD para direccionarla a la mia en MySQL. Pero, puedes dejar la base de datos por defecto <code>db.sqlite3</code> mientras manejemos el desarrollo.
- Realizar las migraciones de la base de datos utilizando <code>python manage.py makemigrations</code> y <code>python manage.py migrate</code>.

<br/><h3>7. Creación de modelos</h3><hr/>

Definir los modelos de datos utilizando la ORM de Django en el archivo <b>models.py</b> de la aplicación.

<b>¿Qué es un modelo?</b> En Django, un modelo representa una tabla en una base de datos. Define la estructura de los datos que se almacenarán, como los campos (nombre, tipo de dato, etc.) y las relaciones entre ellos. Ejemplo: Imaginemos una aplicación de blog. Un modelo "Post" podría tener campos como "titulo", "contenido", "fecha_publicacion" y "autor".

<b>¿Cómo se crea un modelo?</b> Se define una clase que hereda de models.Model. Se añaden campos como atributos a esta clase, utilizando clases como <code>CharField, TextField, DateTimeField</code>, etc. Se establecen relaciones entre modelos, como "uno a muchos", "muchos a muchos", etc.

```Python
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    pub_date = models.DateTimeField('date published')
```

<b>¿Para qué sirven los modelos?</b>

- Definen la estructura de la base de datos.
- Permiten realizar consultas a la base de datos de forma sencilla.
- Facilitan la validación de datos.

<br/><h3>8. Creación de vistas</h3><hr/>

Crear funciones en el archivo <b>views.py</b> de la aplicación para manejar las solicitudes HTTP.

<b>¿Para qué sirven las vistas?</b>

- Manejan las solicitudes HTTP entrantes.
- Interactúan con los modelos para recuperar o guardar datos.
- Renderizan las plantillas para generar la salida HTML.

<br/><b>¿Qué es una vista?</b> Una vista en Django es una función Python que recibe una solicitud HTTP y devuelve una respuesta HTTP. Es decir, es el enlace entre la URL y la lógica de la aplicación.

<b>¿Cómo se crea una vista?</b> Se define una función en el archivo <b>views.py</b> de una aplicación.

Esta función recibe una solicitud HTTP como argumento y devuelve un objeto de respuesta (por ejemplo, un objeto HttpResponse o un objeto de plantilla renderizado).

```Python
from django.shortcuts import render
from .models import Post

def index(request):
    posts = Post.objects.all()
    return render(request, 'blog/index.html', {'posts': posts})
```

<b>¿Qué hace el código anterior?</b>

- Obtiene todos los objetos Post de la base de datos.
- Pasa estos objetos a una plantilla llamada <code>blog/index.html</code>.
- La función render se encarga de renderizar la plantilla y devolver la respuesta HTTP.

<br/><h3>9. Creación de plantillas</h3>

Crear plantillas HTML para renderizar las vistas utilizando el sistema de plantillas de Django.

<br/><h3>10. Definición de URLs</h3><hr/>

Configurar las URLs de la aplicación en el archivo <b>urls.py</b> de la aplicación y en el archivo <b>urls.py</b> del proyecto.

<br/><h3>11. Ejecución del servidor de desarrollo</h3><hr/>

Ejecutar el servidor de desarrollo utilizando el comando <code>python manage.py runserver</code>.
