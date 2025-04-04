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
   python manage.py migrate
   python manage.py loaddata database.json
   # por facilidad y sólo para uso local
   # utilizar:
   # Username: admin
   # Password: admin
   ```

   ## Ejecución del proyecto
   - Para ejecutar el proyecto se deben ejecutar desde la carpeta de instalación, los siguientes comandos:
      ```bash
      python manage.py runserver
      ```

   - Una vez ejecutado este código la aplicación puede encontrarse en:

      `http://127.0.0.1:8000/sma/` o `http://127.0.0.1:8000/api/`

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
      - [Documento-Presentacion-cliente](https://github.com/mayerlynyrs/gruposiete/blob/main/pdf/1-Presentacion-cliente.pdf)
      - [PPDA-Ejemplos-reporte](https://github.com/mayerlynyrs/gruposiete/blob/main/pdf/2-PPDA-ejemplos-reporte.pdf)
      - [Instrucciones-MMA-reporte-Diario-Oficial](https://github.com/mayerlynyrs/gruposiete/blob/main/pdf/3-200820-Dicta-Instrucciones-MMA.pdf)

   ## Autores

   - [@mayerlynyrs](https://www.github.com/mayerlynyrs)
   - [@puribe](https://www.github.com/puribe)
   - [@bianelbianchini](https://github.com/bianelbianchini)
   - [@eltan-ing](https://github.com/eltan-ing)
   - [@seba2305](https://github.com/seba2305)

