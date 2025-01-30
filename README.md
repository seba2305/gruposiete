# GRUPO7

```
git clone https://github.com/mayerlynyrs/gruposiete.git
cd gruposiete
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

#### Creación de la base de datos

- Crear la base de datos (nombre de la base de datos `grupo7`)


 ```
python manage.py makemigrations
python manage.py migrate
python manage.py loaddata database.json     **json**
``` 
- Para correr el proyecto
```
python manage.py runserver
```

### Ejecución

Una vez ejecutado este código la aplicación puede encontrarse en:

`http://127.0.0.1:8000`


#### .pdf referenciales
## M4-Class2 - Introducción al framework Django
○ Paso 1: Crear y activar el entorno virtual:
`python -m venv venv`
`source venv/bin/activate` # Linux/Mac
`venv\Scripts\activate` # Windows

○ Paso 2: Instalar Django
`pip install django`

○ Paso 3: Crear un proyecto
`django-admin startproject gruposiete`

○ Paso 4: Ejecutar el servidor
`python manage.py runserver`

Crea una aplicación dentro del Proyecto
`python manage.py startapp myapp`

## M4-Class4 - Django Rest Framework
<!-- Extendiendo la API -->
Genera un token para este usuario
`python manage.py drf_create_token <username>`

## M4-Class6 - Construyendo una API en DRF
Configurar drf-spectacular
Paso 1. Instalación: `pip install drf-spectacular`

## M5-Class3 - Acceso a Datos con SQL Nativo en Python
Instalación
>> `pip install psycopg2`
ó en caso de no tener pg_config instalado
>> `pip install psycopg2-binary`
