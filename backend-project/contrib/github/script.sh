#!/bin/sh
set -eux
docker-compose up -d
# verify integration of services
docker-compose run --rm backend bash -c 'wait-for-it -t 600 frontend:8000'
# verify that user able to view login form for admin
[ $(curl  -s -o /dev/null -w '%{http_code}' http://localhost:8000/admin/) -eq '302' ]
# verify that static assets available
[ $(curl  -s -o /dev/null -w '%{http_code}' http://localhost:8000/static/admin/css/base.css) -eq '200' ]
# keep OpenAPI specs for build-artifact
docker-compose run backend python -W ignore manage.py generate_swagger -f yaml > openapi.yaml
docker-compose run backend python -W ignore manage.py generate_swagger -f json > openapi.json
