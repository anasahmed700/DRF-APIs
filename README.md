# Django REST Framework API

A backend RESTful API built with **Django** and **Django REST Framework (DRF)**.

## 🚀 Features

- JWT / Token Authentication
- CRUD APIs using DRF
- Custom permissions and throttling
- API documentation using `drf-yasg` or `drf-spectacular`
- Pagination and filtering
- Environment-based settings with `.env`
- Admin panel for managing models

## 🛠 Tech Stack

- Python 3.8+
- Django 4.x+
- Django REST Framework
- drf-yasg (for Swagger docs) *(optional)*
- PostgreSQL / SQLite / any DB
- Docker (optional)

## 📦 Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/your-username/your-repo.git
cd your-repo
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv
# Windows
.\venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a .env file in the root directory:

```bash
DEBUG=True
SECRET_KEY=your-secret-key
ALLOWED_HOSTS=127.0.0.1,localhost
DATABASE_URL=sqlite:///db.sqlite3
```

### 5. Run migrations

```bash
python manage.py migrate
```

### 6. Start development server

```bash
python manage.py runserver
```

### 7. Access API

Swagger docs: <http://localhost:8000/swagger/>

ReDoc (optional): <http://localhost:8000/redoc/>
