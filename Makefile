.PHONY:build shell
build:
	docker build -t idiomatic-python .
shell: build
	docker run -it idiomatic-python /bin/bash
test: build
	docker run -it idiomatic-python pytest tests/
