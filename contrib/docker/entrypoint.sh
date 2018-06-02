#!/usr/bin/env sh
set -e

python manage.py collectstatic --noinput;
python manage.py migrate --noinput;

exec "$@"