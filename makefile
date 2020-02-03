.PHONY: all deploy lint flake8 tests
# make tests >debug.log 2>&1
ifeq ($(OS),Windows_NT)
PYTHON = venv/Scripts/python.exe
PTEST = venv/Scripts/pytest.exe
GCLOUD = $(LOCALAPPDATA)\Application Data\Google\Cloud SDK\google-cloud-sdk\bin\gcloud.cmd
else
PYTHON = ./venv/Scripts/python
PTEST = ./venv/bin/pytest
GCLOUD = gcloud
endif

S = source
TESTS = tests
LIBDIR = $(S)/libs

PYTEST = $(PTEST) --cov=$(S) --cov-report term:skip-covered --cov-report html
PIP = $(PYTHON) -m pip install
SUB_PATH = submodules/vbot

PROJECT = telegram-notify-text
VERSION = initial

all: tests

test:
	$(PYTEST) -s --cov-append $(TESTS)/test/$(T)

tests: flake8 lint
	$(PYTEST) --durations=5 $(TESTS)

flake8:
	$(PYTHON) -m flake8 --max-line-length=110 --exclude=libs --builtins="_" $(S)
	$(PYTHON) -m flake8 --max-line-length=110 $(TESTS)

lint:
	$(PYTHON) -m pylint $(TESTS)/test
	$(PYTHON) -m pylint --disable=relative-import $(S)

deploy:
	$(GCLOUD) app deploy --quiet --project $(PROJECT) -v $(VERSION) $(S)/app.yaml $(S)/backend.yaml $(S)/index.yaml $(S)/queue.yaml

setup: setup_python setup_pip

setup_pip:
	$(PIP) --upgrade pip
	$(PIP) -r requirements.txt
	$(PIP) -t $(LIBDIR) -r $(LIBDIR)/requirements.txt

setup_python:
	$(PYTHON_BIN) -m virtualenv venv
