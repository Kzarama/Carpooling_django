# Carpooling

To build the images of the project
~~~bash
docker-compose -g local.yml build
~~~
To see the images builded
~~~bash
docker images
~~~
To run the project (create the red, volumes and start the services)
~~~bash
docker-compose -f local.yml up
~~~
To see the images running
~~~bash
docker-compose -f local.yml ps
~~~
To stop the project
~~~bash
docker-compose -f local.yml down
~~~
To run a command of django of manage.py (--rm to delete a container when the command finish)
~~~bash
docker-compose -f local.yml run --rm django COMMAND
~~~
To create a superuser
~~~bash
docker-compose -f local.yml run --rm django python manage.py createsuperuser
~~~

---

## Folders and files
- config = folder that contains the main files of the project
    - settings = folder that contains the configuration of the project
        - base = base of settings of the project
        - local = file of local setting of the project
        - production = file of production of the project
        - test = tests of the project
    - urls = file with the urls of the project
    - wsgi = settings of wsgi for production
- requirements = folder of requirements of the project
    - base = default requirements
    - local = requirements for local run
    - production = requirements for production of the project
- compose = folder of the services that compose the project, declare variables, services... and contains files of docker
    - local
        - Dockerfile = configuration of docker
        - start = variables for propagation of errors and commands for run the project
    - production = 
        - caddy = folder of server https
        - django = 
            - celery = configuration of celery
            - entrypoint = file of python
        - Dockerfile = configuration of docker
- cride = apps of the project
    - taskapp = folder of apps
        - celery = instance of celery
- local = file that declare the services in docker (django, postgres, celery)
- production = file that declare the services in docker for production

---

## To debug django
~~~bash
docker-compose -f local.yml up
~~~
In another terminal
~~~bash
docker-compose -f local.yml ps
~~~
kill django
~~~bash
docker rm -f carpooling_django_1
~~~
To run django in like a only service
~~~bash
docker-compose run --rm --service-port django
~~~
In the file put
~~~python
import ipdb; ipdb.set_trace()
~~~

---

## Delete migrations
First delete a migrations files  
List volumes 
~~~bash
docker volume ls
~~~
Delete volume of postgres
~~~bash
docker volume rm carpooling_local_postgres_data
~~~
Create migration file
~~~bash
docker-compose run --rm django python manage.py makemigrations
~~~
Make changes
~~~bash
docker-compose run --rm django python manage.py migrate
~~~

---

## Serializer
Are containers that allows take types of complex data, then turn then in native data of python for the posterior use like json or xml. 

---

## Modules

- environ = allows make operations with the paths

## Dependencies
- pytz = timezone
- psycopg2 = connection with postgres
- argon2-cffi = password encryption

## Bonus 
export makes a environment variable in the console actual, for only use docker-compose build
~~~bash
export COMPOSE_FILE = local.yml
~~~

HTTPie for do request at the server from the console