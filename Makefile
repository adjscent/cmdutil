lint:
	black .
	isort .
	mypy .

install-dev:
	pip install isort black mypy types-setuptools