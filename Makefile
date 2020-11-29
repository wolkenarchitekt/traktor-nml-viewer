CONTAINER  = traktor-nml-viewer
VIRTUALENV_DIR = .venv
TRAKTOR_DIR ?= "$(HOME)/traktor3"

virtualenv-create:
	python3.7 -m venv $(VIRTUALENV_DIR)
	. $(VIRTUALENV_DIR)/bin/activate && \
		pip install --upgrade setuptools pip && \
		pip install -r requirements.txt && \
		pip install -r requirements-dev.txt && \
		pip install -e .

virtualenv-migrate:
	python3.7 -m venv $(VIRTUALENV_DIR)
	. $(VIRTUALENV_DIR)/bin/activate && \
		python manage.py makemigrations && \
		python manage.py migrate

virtualenv-runserver:
	python3.7 -m venv $(VIRTUALENV_DIR)
	. $(VIRTUALENV_DIR)/bin/activate && \
		python manage.py runserver

virtualenv-shell:
	python3.7 -m venv $(VIRTUALENV_DIR)
	. $(VIRTUALENV_DIR)/bin/activate && \
		python manage.py shell

virtualenv-import-nml:
	python3.7 -m venv $(VIRTUALENV_DIR)
	. $(VIRTUALENV_DIR)/bin/activate && \
		python manage.py traktor_nml_import "$(TRAKTOR_DIR)"
