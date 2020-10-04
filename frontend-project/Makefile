.PHONY: lint
install:
	docker-compose run --rm frontend yarn

.PHONY: lint
build:
	docker-compose run --rm frontend yarn build

.PHONY: lint
lint:
	docker-compose run --rm frontend yarn lint

.PHONY: test
test:
	docker-compose run --rm frontend yarn test

.PHONY: fmt
fmt:
	docker-compose run --rm frontend yarn prettier
