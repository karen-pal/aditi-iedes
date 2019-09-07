# Instalar:

Para ejecutar el proyecto primero vamos a necesitar tres cosas:

    * Docker (https://www.docker.com/)
    * Python: (http://python.org)
    * Virtualenv (https://virtualenv.pypa.io/en/latest/)

Una vez instalado todo, vamos a crear un entorno virtual en nuestra carpeta de trabajo

    $ virtualenv -p python3 my-env
    $ source ./my-env/bin/activate
    (my-env) $

Luego vamos a instalar `docker-compose`:

    (my-env) $ pip install docker-compose
    ...
    (my-env) $

# Build:

Para construir las imágenes debemos ejecutar el siguiente comando:

    (my-env) $ docker-compose build

# Ejecutar el servidor de desarrollo

Para ejecutar el servidor de desarrollo vamos a correr el siguiente comando:

    (my-env) $ docker-compose up
