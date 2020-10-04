#!/bin/sh
set -eux
# verify integration of services
docker-compose up -d
make wait_frontend wait_backend
# verify that user able to view login form for admin
[ $(curl  -s -o /dev/null -w '%{http_code}' http://localhost:8000/) -eq '200' ]
# verify that user able to view login form for admin
[ $(curl  -s -o /dev/null -w '%{http_code}' http://localhost:8000/admin/) -eq '302' ]
# verify that static assets available
[ $(curl  -s -o /dev/null -w '%{http_code}' http://localhost:8000/static/admin/css/base.css) -eq '200' ]