# Run tests with pytest
test:
	pytest --tb=short

# Apply database migrations
migrate:
	python manage.py migrate

# Run the development server
runserver:
	python manage.py runserver

# Open Django shell
shell:
	python manage.py shell

# Install dependencies
install:
	pip install -r requirements.txt