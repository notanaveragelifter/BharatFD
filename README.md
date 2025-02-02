# FAQ Management System

This is a Django-based FAQ management system that allows you to store, manage, and retrieve FAQs with multi-language translation support. It includes a REST API, caching with Redis, and a user-friendly admin interface.

---

## Features
- **FAQ Management**: Store FAQs with questions and answers.
- **Multi-language Support**: Automatically translate FAQs into multiple languages (e.g., Hindi, Bengali) using the Google Translate API.
- **WYSIWYG Editor**: Use a rich text editor (CKEditor) to format answers.
- **REST API**: Fetch FAQs in different languages via API.
- **Caching**: Improve performance with Redis caching for translations.
- **Admin Panel**: Manage FAQs through Django’s admin interface.
- **Unit Tests**: Ensure code quality with unit tests.

---

## Prerequisites
Before you begin, ensure you have the following installed:
- Python 3.9 or higher
- Redis
- Git

---

## Installation

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/faq-project.git
cd faq-project

# README

## Set Up a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

## Install Dependencies
```bash
pip install -r requirements.txt
```

## Set Up the Database
Run migrations to create the database tables:
```bash
python manage.py migrate
```

## Create a Superuser
Create an admin account to access the Django admin panel:
```bash
python manage.py createsuperuser
```

## Start Redis
Ensure Redis is running on your system. You can start it with:
```bash
redis-server
```

## Running the Project
### Start the Development Server
```bash
python manage.py runserver
```

### Access the Admin Panel
Open your browser and go to [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/).
Log in with the superuser credentials you created earlier.

### Add FAQs
In the admin panel, click on FAQs and add some FAQs with questions and answers.
The system will automatically translate the FAQs into Hindi and Bengali (if translations are available).

## API Usage
### Fetch FAQs
You can fetch FAQs in different languages using the API.

#### Fetch FAQs in English (default)
```bash
curl http://127.0.0.1:8000/api/faqs/
```

#### Fetch FAQs in Hindi
```bash
curl http://127.0.0.1:8000/api/faqs/?lang=hi
```

#### Fetch FAQs in Bengali
```bash
curl http://127.0.0.1:8000/api/faqs/?lang=bn
```

## Testing
### Run Unit Tests
To ensure everything is working correctly, run the unit tests:
```bash
pytest
```

## Configuration
### Redis Caching
The project uses Redis for caching translations. Ensure Redis is running on your system. You can configure the Redis connection in `settings.py`:
```python
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}
```

### Google Translate API
The project uses the `googletrans` library for translations. If translations fail, the system will fall back to English.

## Project Structure
```
faq_project/
├── faq/                <-- Django app for FAQs
│   ├── migrations/     <-- Database migrations
│   ├── admin.py        <-- Admin panel configuration
│   ├── models.py       <-- Database models
│   ├── serializers.py  <-- API serializers
│   ├── views.py        <-- API views
│   ├── tests.py        <-- Unit tests
│   └── ...
├── faq_project/        <-- Project settings and configuration
│   ├── settings.py     <-- Django settings
│   ├── urls.py         <-- URL routing
│   └── ...
├── manage.py           <-- Django command-line tool
├── requirements.txt    <-- Python dependencies
└── README.md           <-- This file
```

## Contributing
1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add your feature"
   ```
4. Push to the branch:
   ```bash
   git push origin feature/your-feature-name
   ```
5. Open a pull request.

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

## Acknowledgments
- [Django](https://www.djangoproject.com/)
- [Django REST Framework](https://www.django-rest-framework.org/)
- [CKEditor](https://ckeditor.com/)
- [Redis](https://redis.io/)
- [Google Translate API](https://pypi.org/project/googletrans/)

