#!/bin/sh
# keep OpenAPI specs for build-artifact
set -eux
docker-compose run backend python -W ignore manage.py generate_swagger -f yaml > openapi.yaml
docker-compose run backend python -W ignore manage.py generate_swagger -f json > openapi.json
