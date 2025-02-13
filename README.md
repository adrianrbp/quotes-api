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
   python -m venv .venv
   source .venv/bin/activate  # Windows: .venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

4. **Apply database migrations:**
   ```sh
   python manage.py migrate
   ```

6. **Create a superuser (optional):**
   ```sh
   python manage.py createsuperuser
   ```

## Running the Application

1. **Start the development server:**
   ```sh
   python manage.py runserver
   ```

Once the server is running, you can access the API at:
- `http://127.0.0.1:8000/api/`

### API Endpoints
- `GET /api/quotes/` - Retrieve all quotes

## Running Tests

1. **Run tests with pytest:**
   ```sh
   pytest
   ```

2. **Generate a coverage report:**
   ```sh
   pytest --cov=quotes
   ```

