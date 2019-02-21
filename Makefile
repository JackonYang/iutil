PY?=python3
PIP?=pip3


dev-setup:
	$(PIP) install -r requirements-dev.txt


build:
	$(PY) setup.py sdist bdist_wheel

upload:
	twine upload dist/*

install:
	$(PIP) install -e .



test:
	pytest .

.PHONY: build upload install
.PHONY: test
.PHONY: dev-setup
