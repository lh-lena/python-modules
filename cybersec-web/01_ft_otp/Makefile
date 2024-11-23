ENV_DIR := env

all: make

make:
	@echo [Creating virtual environment ...]
	@python3 -m venv $(ENV_DIR)
	@echo [Installing dependencies ...]
	@python3.11 -m pip install --upgrade pip
	$(ENV_DIR)/bin/pip3 install -r requirements.txt
	@chmod +x ft_opt.py
	@echo [Setup complete. Activate environment using: ". $(ENV_DIR)/bin/activate"]

# Clean environment
clean:
	@echo [Removing virtual environment ...]
	@rm -rf $(ENV_DIR)
	@echo [Done!]

re: clean make

.PHONY: all make clean 

# Activate environment
#. env/bin/activate