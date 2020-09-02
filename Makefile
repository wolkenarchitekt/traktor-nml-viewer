CONTAINER  = traktor-nml-viewer
VIRTUALENV_DIR = .venv

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
		pip install --upgrade setuptools pip && \
		pip install -r requirements.txt && \
		pip install -r requirements-dev.txt && \
		pip install -e .
