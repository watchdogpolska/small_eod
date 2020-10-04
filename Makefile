TEST?=small_eod

.PHONY: start
start: wait_mysql wait_minio
	docker-compose up -d

.PHONY: stop
stop:
	docker-compose stop

.PHONY: clean
clean:
	docker-compose down

.PHONY: build
build:
	docker-compose build

.PHONY: test
test: backend_test frontend_test

.PHONY: lint
lint: backend_lint frontend_lint

.PHONY: check
check: backend_check

.PHONY: logs
logs:
	docker-compose logs --tail 100 -f

# Waiters
.PHONY: wait_mysql
wait_mysql:
	docker-compose up -d db
	docker-compose run --rm backend bash -c 'wait-for-it db:5432'

.PHONY: wait_minio
wait_minio:
	docker-compose up -d minio
	docker-compose run --rm backend bash -c 'wait-for-it minio:9000'

.PHONY: wait_frontend
wait_frontend:
	docker-compose up -d frontend
	docker-compose run --rm backend bash -c 'wait-for-it -t 200 frontend:8000'

.PHONY: wait_backend
wait_backend: wait_mysql wait_minio
	docker-compose up -d backend
	docker-compose run --rm backend bash -c 'wait-for-it backend:8000'

# Back-end section
# All targets should start with "backend_"
.PHONY: backend_test
backend_test:
	make -C backend-project test

.PHONY: backend_lint
backend_lint:
	make -C backend-project lint

.PHONY: fmt
backend_fmt:
	make -C backend-project fmt

.PHONY: backend_check
backend_check: wait_mysql wait_minio
	make -C backend-project check

.PHONY: backend_migrate
backend_migrate:
	make -C backend-project migrate

.PHONY: backend_migrations
backend_migrations:
	make -C backend-project migrations

# Frontend section
# All targets should start with "frontend_"
.PHONY: frontend_build
frontend_build:
	make -C frontend-project build

.PHONY: frontend_lint
frontend_lint:
	make -C frontend-project lint

.PHONY: frontend_test
frontend_test:
	make -C frontend-project test

.PHONY: frontend_fmt
frontend_fmt:
	make -C frontend-project fmt

.PHONY: frontend_install
frontend_install:
	make -C frontend-project install

# Balancer section
# All targets should start with "balancer_"
.PHONY: balancer_build
balancer_build:
	make -C balancer build

.PHONY: balancer_push
balancer_push:
	make -C balancer push
