#!/bin/sh

python manage.py migrate || exit 1
gunicorn appeals.wsgi:application --bind 0.0.0.0:8080 --reload --log-level DEBUG
