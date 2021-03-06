#!/bin/sh

if [ "$DOCKER" = 1 ]
then
    echo "Waiting for postgres..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
    python manage.py flush --no-input
    python manage.py migrate
    python manage.py loaddata datadump.json
fi


exec "$@"