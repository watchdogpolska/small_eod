#!/bin/bash
# Add superuser to backend using default credentials:
# login: root
# password: root
set -eux
make wait_minio
docker-compose run --rm -e DJANGO_SUPERUSER_PASSWORD=root backend python manage.py createsuperuser --username root --email root@example.com --noinput