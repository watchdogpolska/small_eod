.PHONY: all test clean docs

TEST?=small_eod

start: wait_mysql wait_minio
	docker-compose up -d

stop:
	docker-compose stop

logs:
	docker-compose logs --tail 100 -f

clean:
	docker-compose down

build:
	docker-compose build backend

test: wait_mysql wait_minio test-django-backend test-openapi-spec

test-django-backend:
	docker-compose run backend python manage.py test --keepdb --verbosity=2 ${TEST}

test-openapi-spec:
	docker-compose run --rm backend python manage.py generate_swagger --format json -o openapi.json
	docker run -v $$(pwd)/backend-project/openapi.json:/openapi.json --rm p1c2u/openapi-spec-validator --schema 2.0 /openapi.json
	docker-compose run --rm backend rm openapi.json

wait_mysql:
	docker-compose up -d db
	docker-compose run --rm backend bash -c 'wait-for-it db:5432'

wait_minio:
	docker-compose up -d minio
	docker-compose run --rm backend bash -c 'wait-for-it minio:9000'

migrate:
	docker-compose run --rm backend python manage.py migrate

makemigrations:
	docker-compose run --rm backend python manage.py makemigrations

lint:
	pre-commit run --all-files

fmt:
	docker run --rm -v /$$(pwd):/data cytopia/black ./backend-project

check: wait_mysql wait_minio
	docker-compose run --rm backend python manage.py makemigrations --check

migrations: wait_mysql wait_minio
	docker-compose run --rm backend python manage.py makemigrations

settings:
	docker-compose run --rm backend python manage.py diffsettings

createsuperuser: wait_minio
	docker-compose run --rm -e DJANGO_SUPERUSER_PASSWORD=root backend python manage.py createsuperuser --username root --email root@example.com --noinput

test-local: lint build check test

openapi:
	docker-compose run --rm backend python manage.py generate_swagger
