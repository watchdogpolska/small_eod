#!/bin/sh
set -eux
docker-compose up -d db nginx
make wait_mysql
# verify that user able to create user
docker-compose run web python manage.py createsuperuser --username root --email root@example.com --noinput
# run test suite
make test
# verify integration of services
docker-compose up -d web
sleep 5 # for http server start
# verify that user able to view login form
curl http://localhost:8000/ -s
# verify that static assets available for nginx
[ $(curl  -s -o /dev/null -w '%{http_code}' localhost:8000/static/admin/css/base.css) -eq '200' ]