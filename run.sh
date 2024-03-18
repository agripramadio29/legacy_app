#!/bin/sh

python3 manage.py collectstatic --noinput
gunicorn legacy_app.wsgi:application --bind 0.0.0.0:8000 --access-logfile gunicorn_stdout.log --error-logfile gunicorn_stderr.log &