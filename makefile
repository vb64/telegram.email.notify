.PHONY: all setup
# make tests >debug.log 2>&1
ifeq ($(OS),Windows_NT)
GCLOUD = $(LOCALAPPDATA)\Google\Cloud SDK\google-cloud-sdk\bin\gcloud.cmd
PYTHON = venv/Scripts/python.exe
PTEST = venv/Scripts/pytest.exe
COVERAGE = venv/Scripts/coverage.exe
else
GCLOUD = gcloud
PYTHON = ./venv/bin/python
PTEST = ./venv/bin/pytest
COVERAGE = ./venv/bin/coverage
endif

SOURCE = source
TESTS = tests
DFLT = $(SOURCE)/default
BACK = $(SOURCE)/backend

PIP = $(PYTHON) -m pip install
DEPLOY = $(GCLOUD) app deploy --project
FLAKE8 = $(PYTHON) -m flake8
LINT = $(PYTHON) -m pylint
PEP257 = $(PYTHON) -m pep257
PYTEST = $(PTEST) --cov=$(SOURCE) --cov-report term:skip-covered

PRJ = text-transform-198104
VERSION = py3
VERSION_BACK = py3b-01

all: tests

test:
	$(PTEST) -s $(TESTS)/test/$(T)

tests: flake8 pep257 lint
	$(PYTEST) --durations=5 $(TESTS)
	$(COVERAGE) html --skip-covered

flake8:
	$(FLAKE8) $(DFLT)
	$(FLAKE8) $(BACK)
	$(FLAKE8) $(TESTS)/test

pep257:
	$(PEP257) $(DFLT)
	$(PEP257) $(BACK)
	$(PEP257) --match='.*\.py' $(TESTS)/test

lint:
	$(LINT) $(DFLT)
	$(LINT) $(BACK)
	$(LINT) $(TESTS)/test

deploy:
	$(DEPLOY) $(PRJ) --version $(VERSION) $(DFLT)/app.yaml

deployback:
	$(DEPLOY) $(PRJ) --version $(VERSION_BACK) $(BACK)/app.yaml

cron:
	$(DEPLOY) $(PRJ) $(SOURCE)/cron.yaml

setup: setup_python setup_pip

setup_pip:
	$(PIP) --upgrade pip
	$(PIP) -r $(DFLT)/requirements.txt
	$(PIP) -r $(TESTS)/requirements.txt

setup_python:
	$(PYTHON_BIN) -m venv ./venv
