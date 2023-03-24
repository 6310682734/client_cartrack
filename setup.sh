#!/bin/sh
if [ -f .env ]; then
    export $(echo $(cat .env | sed 's/#.*//g'| xargs) | envsubst)
    python3 manage.py migrate
    python3 manage.py createsuperuser --noinput
fi