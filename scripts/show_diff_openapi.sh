#!/bin/bash
set -eux
REFERENCE_OPENAPI="https://dev.small-eod.siecobywatelska.pl/api/swagger.json"
diff -c -C 10 <( curl -s "${REFERENCE_OPENAPI}"  | jq '.') <( docker-compose run -T --rm backend python manage.py generate_swagger --format json | jq '.' )
