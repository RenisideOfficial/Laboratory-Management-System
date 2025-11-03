# 🧪 Laboratory Management System

_A modern backend solution for laboratory operations management_

[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-2.0+-green.svg)](https://flask.palletsprojects.com/)
[![MySQL](https://img.shields.io/badge/MySQL-8.0-orange.svg)](https://mysql.com)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## 📋 Overview

The **Laboratory Management System (LMS)** is a robust backend API built with Flask and MySQL, designed to streamline laboratory operations including test management, sample tracking, inventory control, and user management.

## ✨ Features

- **🔬 Test Management** - Create, track, and manage laboratory tests
- **🧫 Sample Tracking** - End-to-end sample lifecycle management
- **📊 Results Management** - Record and update test results
- **👥 User Management** - Role-based access control
- **📦 Inventory Control** - Manage laboratory supplies and reagents
- **🔒 RESTful API** - Clean, well-documented endpoints
- **🗄️ Database Migrations** - Version-controlled schema changes
- **⚙️ Configurable** - Environment-specific configurations

## 🛠 Tech Stack

- **Backend Framework**: Flask
- **Database**: MySQL
- **ORM**: SQLAlchemy
- **Migrations**: Alembic
- **Language**: Python 3.7+
- **API**: RESTful architecture

## 🚀 Quick Start

### Prerequisites

- Python 3.7 or higher
- MySQL 8.0 or compatible database
- pip package manager

### Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/RenisideOfficial/Laboratory-Management-System.git
   cd Laboratory-Management-System
   ```

2. **Set up virtual environment**

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Linux/Mac
   # venv\Scripts\activate  # Windows
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment**

   ```bash
   # Copy and edit configuration
   cp config/example.py config/development.py
   # Update with your database credentials
   ```

5. **Run database migrations**

   ```bash
   alembic upgrade head
   ```

6. **Start the application**

   ```bash
   flask run --port=8000
   # or
   python main.py --port=8000
   ```

7. **Verify installation**
   ```bash
   curl http://localhost:8000/api/health
   ```

## 📁 Project Structure

```
Laboratory-Management-System/
├── app/                    # Application package
│   ├── models/            # Database models
│   ├── routes/            # API routes
│   ├── services/          # Business logic
│   └── utils/             # Utility functions
├── config/                # Configuration files
│   ├── development.py     # Dev environment config
│   └── production.py      # Prod environment config
├── db/                    # Database scripts
│   └── migrations/        # Alembic migration files
├── tests/                 # Test suite
├── main.py               # Application entry point
├── requirements.txt      # Python dependencies
└── alembic.ini          # Alembic configuration
```

## ⚙️ Configuration

Key environment variables:

```python
MYSQL_HOST=localhost
MYSQL_USER=your_username
MYSQL_PASSWORD=your_password
MYSQL_DB=laboratory_db
FLASK_ENV=development
SECRET_KEY=your_secret_key
```

## 📡 API Endpoints

### Users

- `GET /api/users` - List all users
- `POST /api/users` - Create new user
- `GET /api/users/{id}` - Get user details
- `PUT /api/users/{id}` - Update user

### Tests

- `GET /api/tests` - List laboratory tests
- `POST /api/tests` - Create new test
- `GET /api/tests/{id}` - Get test details
- `PUT /api/tests/{id}` - Update test

### Samples

- `GET /api/samples` - List samples
- `POST /api/samples` - Create new sample
- `GET /api/samples/{id}` - Get sample details
- `PUT /api/samples/{id}` - Update sample status

### Results

- `GET /api/results` - List test results
- `POST /api/results` - Record new result
- `PUT /api/results/{id}` - Update result

## 🧪 Development

### Running Tests

```bash
pytest tests/
```

### Code Formatting

```bash
black app/ tests/
flake8 app/ tests/
```

### Database Operations

```bash
# Create new migration
alembic revision --autogenerate -m "description"

# Apply migrations
alembic upgrade head

# Rollback migration
alembic downgrade -1
```

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guidelines](CONTRIBUTING.md) for details.

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👥 Authors

- **Reniside** - _Initial work_ - [RenisideOfficial](https://github.com/RenisideOfficial)

## 🙏 Acknowledgments

- Flask community for excellent documentation and examples
- SQLAlchemy and Alembic teams for robust database tools
- Contributors and testers

---

## 📞 Support

If you have any questions or run into issues, please open an issue on GitHub or contact the development team.

---

<div align="center">
  
**Built with ❤️ by [Reniside](https://github.com/RenisideOfficial)**

</div>
