
venv:
	python -m venv .venv
	@echo "Run 'source .venv/bin/activate' on Linux/Mac or '.venv\Scripts\activate' on Windows"

# Run tests with pytest
test:
	pytest --tb=short

# Apply database migrations
migrate:
	python manage.py migrate

# Populate the db with n quotes
seed:
	python manage.py seed --count=$(count)

# Run the development server
serve:
	python manage.py runserver

# Open Django shell
shell:
	python manage.py shell

# Install dependencies
install:
	pip install -r requirements.txt

# Generate Swagger Documentation
gendocs:
	python manage.py spectacular --color --file schema.yaml