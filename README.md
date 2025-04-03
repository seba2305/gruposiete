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
pip install django-crum  (porfa pasar esto a los requirements.txt)
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser (por facilidad y sólo para uso local,uso admin:admin)

```

- datos básicos: 
```sql
INSERT INTO public.app_organismosectorial(id, nombre) VALUES (1, 'Servicio de Evaluación Ambiental');
INSERT INTO public.app_organismosectorial(id, nombre) VALUES (2, 'Superintendencia de Electricidad y Combustibles');
INSERT INTO public.app_organismosectorial(id, nombre) VALUES (3, 'Intendencia Regional de Valparaíso');
INSERT INTO public.app_organismosectorial(id, nombre) VALUES (4, 'Dirección General del Territorio Marítimo y de Marina Mercante');
INSERT INTO public.app_organismosectorial(id, nombre) VALUES (5, 'Corporación Nacional Forestal');
INSERT INTO public.app_organismosectorial(id, nombre) VALUES (6, 'Servicio Agrícola y Ganadero');

INSERT INTO public.app_plan (id, nombre,inicio,termino,estado_avance) VALUES (1, 'PLAN DE PREVENCIÓN Y DESCONTAMINACIÓN ATMOSFÉRICA PARA LAS COMUNAS DE CONCÓN, QUINTERO Y PUCHUNCAVÍ', '2025-01-30 18:14:24-03', '2025-12-31 18:14:36-03', '0 %');

INSERT INTO public.app_tipomedida(id, nombre) VALUES (1, 'Medida regulatoria');
INSERT INTO public.app_tipomedida(id, nombre) VALUES (2, 'Medida no regulatoria');

INSERT INTO public.app_verificacion(id, nombre, verificacion) VALUES (1, 'RCA aprobadas', 'Registro de las RCA aprobadas identificando el titular, la RCA, las emisiones y el monto a compensar');


INSERT INTO public.app_verificacion(id, nombre, verificacion) VALUES (2, 'Cumple art 33 SEC', 'Oficialización de la instrucción de SEC para cumplir con el sistema indicado en el artículo 33 del plan');


INSERT INTO public.app_medida(id, referencia_pda, nombre_corto ,indicador,formula_de_calculo, frecuencia_reporte , tipo_de_dato_a_validar, organismo_sectorial_id, plan_id, tipo_medida_id ) VALUES (1, '42,43,44', 'RCA que contenga obligación de compensar emisiones', 'Número de RCA aprobadas en el año t que contengan obligaciones de compensar emisiones atmosféricas', 'Suma del número de RCA aprobadas que contengan obligaciones de compensar emisiones atmosféricas', 'ANUAL', 'numeric', 1, 1, 2);
INSERT INTO public.app_medida(id, referencia_pda, nombre_corto ,indicador,formula_de_calculo, frecuencia_reporte , tipo_de_dato_a_validar, organismo_sectorial_id, plan_id, tipo_medida_id ) VALUES (2, '33,37', 'Requisito del sistema de almacenamiento intermedio', 'Instrucciones de SEC para cumplir con el sistema de almacenamiento intermedio u otro con el mismo objetivo, conforme al artículo 5 de DS n°160/2008', 'Si/No', 'UNICA', 'string', 2, 1, 1);

INSERT INTO public.app_organismoplan VALUES (1, 1, 1);
INSERT INTO public.app_organismoplan VALUES (2, 2, 1);
INSERT INTO public.app_organismoplan VALUES (3, 3, 1);
INSERT INTO public.app_organismoplan VALUES (4, 4, 1);
INSERT INTO public.app_organismoplan VALUES (5, 5, 1);
INSERT INTO public.app_organismoplan VALUES (6, 6, 1);

INSERT INTO public.app_verificacionmedida VALUES (1, 1, 1);
INSERT INTO public.app_verificacionmedida VALUES (2, 2, 2);

INSERT INTO public.app_verificacionmedida VALUES (2, 2, 2);

INSERT INTO public.auth_group ("name") VALUES ('organizacion_sectorial');

commit;

-- esto resetea las secuencias, ya que al insertar directamente el valor de una pk, pierde la sincronIa con la tabla

SELECT SETVAL('app_organismosectorial_id_seq', COALESCE(MAX(id), 1) ) FROM app_organismosectorial;
SELECT SETVAL('app_plan_id_seq', COALESCE(MAX(id), 1) ) FROM app_plan;
SELECT SETVAL('app_tipomedida_id_seq', COALESCE(MAX(id), 1) ) FROM app_tipomedida;
SELECT SETVAL('app_verificacion_id_seq', COALESCE(MAX(id), 1) ) FROM app_verificacion;
SELECT SETVAL('app_medida_id_seq', COALESCE(MAX(id), 1) ) FROM app_medida;



 
```
- Para correr el proyecto
```
python manage.py runserver
```

### Ejecución

Una vez ejecutado este código la aplicación puede encontrarse en:

`http://127.0.0.1:8000/sma/` o `http://127.0.0.1:8000/api/`

Al grupo organizacion_sectorial, se le debe asignar los permisos: 
- App | medida reportada | Can add medida reportada
- App | medida reportada | Can view medida reportada

Para probar si efectivamente funciona o no el token , crear usuario por active admin, luego generar el token

En Postman hacer lo siguiente: 
1. Abrir Postman.
2. Seleccionar el método HTTP (GET, POST, etc.).
3. Ingresar la URL de la API, por ejemplo:
   http://127.0.0.1:8000/sma/organismos/
4. En la pestaña "Headers", agregar:
   Key: Authorization
   Value: Token TU_TOKEN_AQUI
   (Ejemplo: Token 123456789abcdef123456789abcdef)
5. Presionar "Send" y verificar la respuesta.

### Documentación de APIs

Se crea Swagger y postman con cada endpoint, hereda descripción de swagger.

Swagger local: http://127.0.0.1:8000/api/docs/

Swagger públicado en internet: https://app.swaggerhub.com/apis-docs/myorganization-834/api-de_sma/1.0.0#/

Postman:  https://www.postman.com/ubicuacl/grupo7   (reemplazar por su token en API de SMA ->Variables -> apiKey )


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
