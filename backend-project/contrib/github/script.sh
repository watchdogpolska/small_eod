#!/bin/sh
set -eux
make wait_mysql wait_minio migrate
docker-compose up -d
# verify that user able to create user
make createsuperuser
# run test suite
make test
# verify integration of services
sleep 5 # for http server start
# verify that user able to view login form
curl http://localhost:8000/ -s
# verify that static assets available for nginx
[ $(curl  -s -o /dev/null -w '%{http_code}' localhost:8000/static/admin/css/base.css) -eq '200' ]
# keep OpenAPI specs for build-artifact
docker-compose run backend python -W ignore manage.py generate_swagger -f yaml > openapi.yaml
docker-compose run backend python -W ignore manage.py generate_swagger -f json > openapi.json
