SHELL:=/bin/bash

start:
	docker-compose up --build

test:
	pip install -r backend_server/requirements.txt
	pytest

stop:
	docker-compose down

clean:
	docker-compose down -v
