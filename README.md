# Proyecto API SMA (GRUPO7)
   Este es un proyecto realizado en el curso "Desarrollo Aplicaciones Back-End Python-TalentoFuturo", el cual busca cubrir la necesidad de registrar y reportar medidas de avance de los diferentes PPDA por parte de los organismos sectoriales.

   #### Tecnologías utilizadas
   Las tecnologías utilizadas en este proyecto fueron las siguientes:
      
      - Lenguaje: Python
      - Base de Datos: PostgreSQL
      - Framework: Django
      - Versionamiento: GIT
      - Gestión del proyecto: Taiga

   

   ## Clonado e Instalación del proyecto

   - Para comenzar con la preparación e instalación del proyecto, debera ejecutar los siguiente comandos en la maquina en la cual se desplegará:

   ```bash
   # Clonamos el repositorio
   git clone https://github.com/mayerlynyrs/gruposiete.git
   # Acceder a la carpeta
   cd gruposiete
   # Crear y activar entorno virtual
   python -m venv .venv
   # Linux/Mac
   source venv/bin/activate
   # Windows
   .venv\Scripts\activate
   # instalacion de librerias
   pip install -r requirements.txt
   ```

   ## Creación de la base de datos y ejecución de migraciones

   - Crear la base de datos (nombre de la base de datos `grupo7`) en PostgreSQL.
   - En caso de ser necesario, deberá editar el archivo ".env", para setear el usuario y password de la Base de Datos.
   - Luego ejecutar los siguientes comandos:

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   python manage.py createsuperuser 
   # por facilidad y sólo para uso local
   # utilizar: 
   #     admin:admin
   ```

   - Datos básicos: 
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

   -- esto resetea las secuencias, ya que al insertar directamente el valor de una pk, pierde la sincronia con la tabla

   SELECT SETVAL('app_organismosectorial_id_seq', COALESCE(MAX(id), 1) ) FROM app_organismosectorial;
   SELECT SETVAL('app_plan_id_seq', COALESCE(MAX(id), 1) ) FROM app_plan;
   SELECT SETVAL('app_tipomedida_id_seq', COALESCE(MAX(id), 1) ) FROM app_tipomedida;
   SELECT SETVAL('app_verificacion_id_seq', COALESCE(MAX(id), 1) ) FROM app_verificacion;
   SELECT SETVAL('app_medida_id_seq', COALESCE(MAX(id), 1) ) FROM app_medida;
   ```

   ## Ejecución del proyecto
   - Para ejecutar el proyecto se deben ejecutar desde la carpeta de instalación, los siguientes comandos:
      ```bash
      python manage.py runserver
      ```

   - Una vez ejecutado este código la aplicación puede encontrarse en:

      `http://127.0.0.1:8000/sma/` o `http://127.0.0.1:8000/api/`

   - Desde el Admin de Django al grupo organizacion_sectorial, se le deben asignar los siguientes permisos: 
      - App | medida reportada | Can add medida reportada
      - App | medida reportada | Can view medida reportada

   - Para probar si efectivamente si funciona o no el token , crear usuario por active admin, luego generar el token.

   - Luego en Postman seguir los pasos a continuación: 
      1. Abrir Postman.
      2. Seleccionar el método HTTP (GET, POST, etc.).
      3. Ingresar la URL de la API, por ejemplo:
         http://127.0.0.1:8000/sma/organismos/
      4. En la pestaña "Headers", agregar:
         - Key: Authorization
         - Value: Token [AQUI_VA_EL_TOKEN]
         (Ejemplo: Token 123456789abcdef123456789abcdef)
      5. Presionar "Send" y verificar la respuesta.

   ## Documentación

   - La documentación acerca de los endpoints fue generada con Swagger. Para acceder a ésta, la podemos encontrar en distintas fuentes:

      - [Swagger local](http://127.0.0.1:8000/api/docs/) (debe estar corriendo el proyecto)

      - [Swagger públicado en internet](https://app.swaggerhub.com/apis-docs/myorganization-834/api-de_sma/1.0.0#/)

      - [Postman](https://www.postman.com/ubicuacl/grupo7) (reemplazar por su token en API de SMA ->Variables -> apiKey )

   - Por otro lado, para poder acceder a la documentación en la cual se baso este proyecto, puede acceder a los siguientes enlaces:

      - [Documento-Presentacion-cliente](https://github.com/mayerlynyrs/gruposiete/pdf/1-Presentacion-cliente.pdf)
      - [PPDA-Ejemplos-reporte](https://github.com/mayerlynyrs/gruposiete/pdf/2-PPDA-ejemplos-reporte.pdf)
      - [Instrucciones-MMA-reporte-Diario-Oficial](https://github.com/mayerlynyrs/gruposiete/pdf/3-200820-Dicta-Instrucciones-MMA.pdf)

   ## Autores

   - [@mayerlynyrs](https://www.github.com/mayerlynyrs)
   - [@puribe](https://www.github.com/puribe)
   - [@bianelbianchini](https://github.com/bianelbianchini)
   - [@eltan-ing](https://github.com/eltan-ing)
   - [@seba2305](https://github.com/seba2305)

