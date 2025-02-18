
venv:
	python -m venv .venv
	@echo "Run 'source .venv/bin/activate' on Linux/Mac or '.venv\Scripts\activate' on Windows"

# Run tests with pytest
test:
	pytest --tb=short

show_urls:
	python manage.py show_urls

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
	python manage.py shell_plus

# Install dependencies
install:
	pip install -r requirements.txt

# Generate Swagger Documentation
gendocs:
	python manage.py spectacular --color --file schema.yaml

# Run Ruff linter (like flake8)
lint:
	ruff check .

# Format code with Ruff (like black)
format:
	ruff format .

# Run both linting and formatting
lint-fix:
	ruff check . --fix