install:
	poetry install

run-local:
	poetry run alembic upgrade head
	poetry run uvicorn src.api.app:app --host 0.0.0.0 --port 8000 --reload --reload-dir . --log-config=log_config.ini --log-level=debug

build:
	poetry run docker-compose -f docker-compose.$(for).yml build

start:
	poetry run docker-compose -f docker-compose.$(for).yml up --force-recreate --remove-orphans

up:
	poetry run docker-compose -f docker-compose.$(for).yml up --force-recreate --remove-orphans -d

stop:
	poetry run docker-compose -f docker-compose.$(for).yml stop

rm:
	poetry run docker-compose -f docker-compose.$(for).yml rm
	sudo rm -rf db

revision:
	poetry run docker run app /bin/bash -c "poetry run alembic revision --autogenerate"

upgrade:
	poetry run docker run app /bin/bash -c "poetry run alembic upgrade $(revision)"

downgrade:
	poetry run docker run app /bin/bash -c "poetry run alembic downgrade $(revision)"

test:
	poetry run docker-compose -f docker-compose.test.yml up --force-recreate --remove-orphans --abort-on-container-exit

test-local:
	poetry run alembic upgrade head
	poetry run pytest -s --verbose

lint:
	poetry run flake8
	poetry run mypy -p src --cache-dir=/dev/null --config-file=pyproject.toml
	poetry run mypy -p tests --cache-dir=/dev/null --config-file=pyproject.toml
