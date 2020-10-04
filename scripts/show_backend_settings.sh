#!/bin/bash
# Show backend settings
set -eux
docker-compose run --rm backend python manage.py diffsettings
