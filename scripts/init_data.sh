#!/bin/bash
# Initialize backend with dummy data
set -eux
make wait_backend
docker-compose run backend python manage.py init_data
