ENV_DIR := env

all: make

make:
	@echo [Creating virtual environment ...]
	@python3 -m venv $(ENV_DIR)
	@echo [Installing dependencies ...]
#@python3 -m pip install --upgrade pip
	$(ENV_DIR)/bin/pip install -r requirements.txt
	@chmod +x spider.py
	@echo [Setup complete. Activate environment using: ". $(ENV_DIR)/bin/activate"]

clean:
	@echo [Removing virtual environment ...]
	@rm -rf $(ENV_DIR)
	@echo [Done!]

re: clean make

.PHONY: all make clean 
