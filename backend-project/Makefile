# Standard target
.PHONY: test
test:
	docker-compose run backend coverage run manage.py test --keepdb --verbosity=2 ${TEST}

.PHONY: lint
lint:
	docker run --rm -v $$(pwd):/apps alpine/flake8 .
	docker run --rm -v $$(pwd):/data cytopia/black --check .

.PHONY: fmt
fmt:
	docker run --rm -v $$(pwd):/data quay.io/watchdogpolska/pyupgrade --py37-plus
	docker run --rm --user $$(id -u):$$(id -u) -v $$(pwd):/data cytopia/black .

.PHONY: check
check:
	docker-compose run --rm backend python manage.py makemigrations --check

# Custom targets
.PHONY: migrate
migrate:
	docker-compose run --rm backend python manage.py migrate

.PHONY: migrations
migrations:
	docker-compose run --rm backend python manage.py makemigrations

# Target non-exposed in /Makfile
.PHONY: coverage_html
coverage_html:
	docker-compose run backend coverage html

.PHONY: coverage_send
coverage_send:
	docker-compose run -e GITHUB_ACTIONS -e GITHUB_REF -e GITHUB_SHA -e GITHUB_HEAD_REF -e GITHUB_REPOSITORY -e GITHUB_RUN_ID -e GITHUB_TOKEN -e COVERALLS_REPO_TOKEN backend coveralls
