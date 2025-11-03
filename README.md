# 🧪 Laboratory Management System

_A Flask backend for laboratory test and patient management_

[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-2.0+-green.svg)](https://flask.palletsprojects.com/)
[![MySQL](https://img.shields.io/badge/MySQL-8.0-orange.svg)](https://mysql.com)

## 📋 Overview

A Flask-based Laboratory Management System that provides APIs for managing users, patients, laboratory tests, and test results. Built with MySQL and JWT authentication.

## 🚀 Quick Start

### Prerequisites

- Python 3.7+
- MySQL 8.0+

### Installation

1. **Clone and setup**

```bash
git clone https://github.com/RenisideOfficial/Laboratory-Management-System.git
cd Laboratory-Management-System
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
pip install -r requirements.txt
```

2. **Configure database**

```python
# Update config/config.py with your MySQL credentials
MYSQL_URL = "mysql+pymysql://username:password@localhost:3306/lab_management"
```

3. **Initialize database**

```bash
python db/db.py
```

4. **Run the application**

```bash
python app.py
```

## 📡 API Endpoints

### 🔐 Authentication

- **POST** `/api/auth/register` - Register new user
- **POST** `/api/auth/login` - User login (returns JWT token)

### 👥 Patient Management

- **POST** `/api/patients` - Create new patient
- **GET** `/api/patients` - Get all patients
- **GET** `/api/patients/{id}` - Get specific patient
- **PUT** `/api/patients/{id}` - Update patient details
- **DELETE** `/api/patients/{id}` - Delete patient

### 🧪 Test Management

- **POST** `/api/tests` - Create new test for patient
- **GET** `/api/tests` - Get all tests
- **GET** `/api/tests/{id}` - Get specific test
- **PUT** `/api/tests/{id}` - Update test results/status

### 📊 Results

- **GET** `/api/patients/{id}/results` - Get all test results for a patient

## 🔐 Authentication

Include JWT token in request headers:

```http
Authorization: Bearer <your_jwt_token>
```

## 📁 Project Structure

```
Laboratory-Management-System/
├── app.py                    # Main application
├── config/
│   └── config.py             # Configuration
├── db/
│   └── db.py                 # Database initialization
├── internal/
│   ├── models/
│   │   ├── user_models.py    # User model
│   │   ├── patient_models.py # Patient model
│   │   └── test_models.py    # Test model
│   ├── routes/
│   │   ├── user_routes.py    # Authentication endpoints
│   │   ├── patient_routes.py # Patient-related endpoints
│   │   ├── test_routes.py    # Test-related endpoints
│   │   └── user_routes.py    # User-related endpoints
│   ├── services/
│   │   ├── user_service.py   # Auth logic (login, register)
│   │   ├── patient_service.py# Patient-related logic
│   │   └── test_service.py   # Test-related logic
│   └── middleware/
│       ├── middleware.py# JWT or session checks
├── migrations/               # Database migration scripts (Alembic)
├── utils/                    # Utility/helper functions
├── requirements.txt
├── alembic.ini               # Alembic configuration
└── README.md

```

## 🗄️ Database Models

### User

- `id`, `full_name`, `email`, `password_hash`, `role`
- Authentication and authorization

### Patient

- `id`, `name`, `date_of_birth`, `gender`, `contact_info`, `created_by`
- Patient demographic information

### Test

- `id`, `test_name`, `patient_id`, `status`, `result`, `performed_by`
- Laboratory test assignments and results

## 📝 Usage Examples

### Register User

```bash
curl -X POST http://localhost:5000/api/auth/register \
  -H "Content-Type: application/json" \
  -d '{
    "full_name": "John Doe",
    "email": "john@lab.com",
    "password": "secret123",
    "role": "doctor"
  }'
```

### Create Patient

```bash
curl -X POST http://localhost:5000/api/patients \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer <your_token>" \
  -d '{
    "name": "Alice Smith",
    "date_of_birth": "1985-05-15",
    "gender": "Female",
    "contact_info": "alice@email.com"
  }'
```

### Assign Test

```bash
curl -X POST http://localhost:5000/api/tests \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer <your_token>" \
  -d '{
    "test_name": "Blood Count",
    "patient_id": 1,
    "status": "pending"
  }'
```

### Update Test Result

```bash
curl -X PUT http://localhost:5000/api/tests/1 \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer <your_token>" \
  -d '{
    "result": "Normal",
    "status": "completed"
  }'
```

### Get Patient Results

```bash
curl -X GET http://localhost:5000/api/patients/1/results \
  -H "Authorization: Bearer <your_token>"
```

## ⚙️ Configuration

Key settings in `config/config.py`:

```python
class Config:
    MYSQL_URL = "mysql+pymysql://user:pass@localhost:3306/lab_management"
    SECRET_KEY = "your-secret-key-for-jwt"
```

## 🔧 Development

Run in development mode:

```bash
python app.py
```

The API will be available at `http://localhost:5000`

---

<div align="center">
  
**Built by [Reniside](https://github.com/RenisideOfficial)**

</div>
