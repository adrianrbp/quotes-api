# Quotes API

An API for managing and retrieving quotes.

## Setup

### Prerequisites
- Python 3.12
- pip
- virtualenv

### Installation

1. **Clone the repository:**
   ```sh
   git clone https://github.com/adrianrbp/quotes-api.git
   cd quotes-api
   ```

2. **Create a virtual environment:**
   ```sh
   python -m venv .venv # make venv
   source .venv/bin/activate  # Windows: .venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```sh
   make install
   ```

4. **Apply database migrations:**
   ```sh
   make migrate
   ```

5. **Populate the db with some sample data:**
   ```sh
   make seed count=10
   ```

6. **Create a superuser (optional):**
   ```sh
   python manage.py createsuperuser
   ```

## Running the Application

1. **Start the development server:**
   ```sh
   make serve
   ```

Once the server is running, you can access the API at:
- `http://127.0.0.1:8000/api/`

### API Endpoints
- `GET /api/quotes/` - Retrieve all quotes
- `POST /api/quotes/` - Create a new quote
- `GET /api/quotes/{id}/` - Retrieve a single quote
- `PUT /api/quotes/{id}/` - Update a quote
- `DELETE /api/quotes/{id}/` - Delete a quote
- `GET /api/quotes/random` - Retrieve a random quote

- [Sample Usage in Curl](REQUESTS.md)

## Running Tests

1. **Run tests with pytest:**
   ```sh
   make test
   ```

2. **Generate a coverage report:**
   ```sh
   pytest --cov=quotes
   ```

## Additional Commands

### Run Linter (flake8-like)
```sh
make lint
```

### Format Code (Black-like)
```sh
make format
```


