#!/bin/sh
export PGPASSWORD='alumnodb'
#A rellenar: escribir alumnodb siempre
dropdb -U alumnodb examen
createdb -U alumnodb examen
python manage.py migrate
python manage.py makemigrations aplicacion
python manage.py migrate

python manage.py createsuperuser

python manage.py populate

python manage.py runserver
