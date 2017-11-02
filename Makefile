.PHONY:build shell test

WORKDIR := /code

build:
	docker build -t idiomatic-python .
shell: build
	docker run -v ${PWD}:${WORKDIR} -it idiomatic-python /bin/bash
test: build
	docker run -it idiomatic-python pytest -v tests/
