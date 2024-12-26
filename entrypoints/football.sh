#!/bin/bash

cd /src

python manage.py migrate
python manage.py add_super_user
python manage.py init_data_to_database

python manage.py collectstatic --noinput

daphne -p 5050 -b 0.0.0.0 football_analytics.asgi:application
