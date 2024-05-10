# API REST para Portafolio

Esta API REST está construida con Django Rest Framework (DRF) y proporciona endpoints para acceder y administrar un portafolio de proyectos. Cada proyecto incluye una descripción y una URL hacia su repositorio en GitHub.

## Instalación

1. Clona este repositorio:

git clone https://github.com/OscarMadera1/api_portafolio.git


2. Instala las dependencias:

pip install -r requirements.txt


3. Realiza las migraciones de la base de datos:

python manage.py migrate


4. Inicia el servidor:

python manage.py runserver

## Endpoints

- "proyecto": "http://oscarmadera.pythonanywhere.com/proyecto/",
- "categoria": "http://oscarmadera.pythonanywhere.com/categoria/",
- "comentario": "http://oscarmadera.pythonanywhere.com/comentario/"
- "Documentación : "https://oscarmadera.pythonanywhere.com/doc/"

## Ejemplo de Uso

### Obtener todos los proyectos

GET /proyectos/

Respuesta:

json
   {
"id": 1,
"titulo": "Tienes un mensaje",
"descripcion": "Este proyecto permite automatizar y generar un mensaje por email a los empleados de una empresa en una plantilla de html personalizada.",
"url": "https://github.com/OscarMadera1/Tienes_un_mensaje",
"fecha_creacion": "2024-04-09T23:51:34.673341Z",
"categoria": 1
},
{
"id": 2,
"titulo": "Acortador url",
"descripcion": "Este proyecto nos permite encriptar las url internas de una compañia, para que solo puedan ser accedidas por los empleados. ademas registrar el nombre de usuario y fecha de acceso a la misma.",
"url": "https://github.com/OscarMadera1/Acortador_Url",
"fecha_creacion": "2024-04-09T23:54:48.199478Z",
"categoria": 2
}

Obtener detalles de un proyecto específico

GET /proyectos/1/
Respuesta:

json
   {
"id": 1,
"titulo": "Tienes un mensaje",
"descripcion": "Este proyecto permite automatizar y generar un mensaje por email a los empleados de una empresa en una plantilla de html personalizada.",
"url": "https://github.com/OscarMadera1/Tienes_un_mensaje",
"fecha_creacion": "2024-04-09T23:51:34.673341Z",
"categoria": 1
}

Contribuciones
¡Las contribuciones son bienvenidas! Si deseas contribuir a este proyecto, por favor abre un issue o envía un pull request.

Contacto
Para cualquier pregunta o comentario, puedes contactarme en omaderanegret@email.com.
