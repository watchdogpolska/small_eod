#!/bin/bash
set -eux
make lint
make build
make check
make test
