# Quote API

Django REST Framework API for managing quotes. Built as a portfolio demonstration project.

## Features

- RESTful API for CRUD operations on quotes
- Built with Django 5.1.1 and Django REST Framework 3.15.2
- SQLite database for development
- Admin interface for easy management

## Prerequisites

- Python 3.8 or higher
- pip (Python package installer)
- Git

## Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/quote-api.git
cd quote-api
```

### 2. Create a Virtual Environment

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run Database Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create a Superuser (Optional)

To access the Django admin panel:

```bash
python manage.py createsuperuser
```

Follow the prompts to create your admin account.

### 6. Run the Development Server

```bash
python manage.py runserver
```

The API will be available at `http://127.0.0.1:8000/`

## API Endpoints

### Quotes

- **List all quotes**: `GET /api/quotes/`
- **Create a quote**: `POST /api/quotes/`
- **Retrieve a quote**: `GET /api/quotes/{id}/`
- **Update a quote**: `PUT /api/quotes/{id}/`
- **Partial update**: `PATCH /api/quotes/{id}/`
- **Delete a quote**: `DELETE /api/quotes/{id}/`

### Admin Panel

Access the Django admin interface at `http://127.0.0.1:8000/admin/`

## API Usage Examples

### Create a Quote

```bash
curl -X POST http://127.0.0.1:8000/api/quotes/ \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Website Redesign",
    "customer_name": "John Doe",
    "total": "5000.00"
  }'
```

### Get All Quotes

```bash
curl http://127.0.0.1:8000/api/quotes/
```

### Get a Specific Quote

```bash
curl http://127.0.0.1:8000/api/quotes/1/
```

### Update a Quote

```bash
curl -X PUT http://127.0.0.1:8000/api/quotes/1/ \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Website Redesign - Updated",
    "customer_name": "John Doe",
    "total": "6000.00"
  }'
```

### Delete a Quote

```bash
curl -X DELETE http://127.0.0.1:8000/api/quotes/1/
```

## Project Structure

```
quote-api/
├── config/              # Project configuration
│   ├── settings.py      # Django settings
│   ├── urls.py          # URL routing
│   ├── wsgi.py          # WSGI config
│   └── asgi.py          # ASGI config
├── quotes/              # Main application
│   ├── models.py        # Database models
│   ├── views.py         # API views
│   ├── serializers.py   # DRF serializers
│   ├── admin.py         # Admin configuration
│   └── tests.py         # Tests
├── manage.py            # Django management script
└── requirements.txt     # Python dependencies
```

## Development

### Running Tests

```bash
python manage.py test
```

### Checking for Issues

```bash
python manage.py check
```

## Technologies Used

- Django 5.1.1
- Django REST Framework 3.15.2
- SQLite (Development)
- Python 3.12+

## License

This project is built for portfolio demonstration purposes.
