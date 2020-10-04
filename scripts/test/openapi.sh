#!/bin/sh

docker-compose run --rm backend python manage.py generate_swagger --format json -o openapi.json
docker run -v $(pwd)/backend-project/openapi.json:/openapi.json --rm p1c2u/openapi-spec-validator --schema 2.0 /openapi.json
docker-compose run --rm backend rm openapi.json