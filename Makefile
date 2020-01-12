.PHONY: all test clean docs

clean:
	docker-compose down

build:
	docker-compose build web

test: wait_mysql wait_minio test-django-backend

test-django-backend:
	docker-compose run web python manage.py test --keepdb --verbosity=2

wait_mysql:
	docker-compose up -d db
	docker-compose run web bash -c 'wait-for-it db:5432'

wait_minio:
	docker-compose up -d minio
	docker-compose run web bash -c 'wait-for-it minio:9000'

migrate:
	docker-compose run web python manage.py migrate

makemigrations:
	docker-compose run web python manage.py makemigrations

pyupgrade:
	docker run --rm -v /$$(pwd):/data quay.io/watchdogpolska/pyupgrade

lint:
	docker run --rm -v /$$(pwd):/apps alpine/flake8 ./backend-project
	docker run --rm -v /$$(pwd):/data cytopia/black --check ./backend-project

fmt:
	docker run --rm -v /$$(pwd):/data cytopia/black ./backend-project

check: wait_mysql
	docker-compose run web python manage.py makemigrations --check

migrations: wait_mysql
	docker-compose run web python manage.py makemigrations

settings:
	docker-compose run web python manage.py diffsettings

createsuperuser:
	docker-compose run web python manage.py createsuperuser --username root --email root@example.com --noinput

test-local: lint build check test
