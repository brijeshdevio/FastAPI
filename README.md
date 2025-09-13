# FastAPI + NeonDB Demo

A modern REST API built with FastAPI and NeonDB (PostgreSQL), featuring user management, product inventory, and feedback collection systems.

## 🚀 Features

- **User Management**: Create and retrieve users with email validation
- **Product Inventory**: Manage products with stock tracking
- **Feedback System**: Collect and store user feedback
- **Database**: PostgreSQL database hosted on NeonDB
- **API Documentation**: Auto-generated interactive API docs with Swagger UI
- **Data Validation**: Pydantic models for request/response validation
- **ORM**: SQLAlchemy for database operations

## 🛠️ Tech Stack

- **Backend**: FastAPI
- **Database**: NeonDB (PostgreSQL)
- **ORM**: SQLAlchemy
- **Validation**: Pydantic
- **Server**: Uvicorn

## 📋 Prerequisites

- Python 3.8+
- NeonDB account and database
- pip or poetry for dependency management

## 🔧 Installation

1. **Clone the repository**:

   ```bash
   git clone <repository-url>
   cd fastapi-neon-demo
   ```

2. **Create a virtual environment**:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
   ```

4. **Set up environment variables**:
   Create a `.env` file in the project root:

   ```env
   DATABASE_URL="postgresql://username:password@host:port/database_name?sslmode=require"
   ```

5. **Initialize the database**:
   ```bash
   python setup.py
   ```

## 🚦 Running the Application

Start the development server:

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

The API will be available at:

- **API**: http://localhost:8000
- **Interactive API Documentation**: http://localhost:8000/docs
- **Alternative API Documentation**: http://localhost:8000/redoc

## 📚 API Endpoints

### Root

- `GET /` - Welcome message

### Users

- `POST /users/` - Create a new user
- `GET /users/` - Get all users

### Products

- `POST /products/` - Create a new product
- `GET /products/` - Get all products

### Feedback

- `POST /feedback/` - Submit feedback
- `GET /feedback/` - Get all feedback

## 📝 API Usage Examples

### Create a User

```bash
curl -X POST "http://localhost:8000/users/" \
     -H "Content-Type: application/json" \
     -d '{"name": "John Doe", "email": "john@example.com"}'
```

### Get All Users

```bash
curl -X GET "http://localhost:8000/users/"
```

### Create a Product

```bash
curl -X POST "http://localhost:8000/products/" \
     -H "Content-Type: application/json" \
     -d '{"product_name": "Laptop", "quantity": 10, "in_stock": true}'
```

### Submit Feedback

```bash
curl -X POST "http://localhost:8000/feedback/" \
     -H "Content-Type: application/json" \
     -d '{"name": "Jane Smith", "comment": "Great service!"}'
```

## 🗄️ Database Schema

### Users Table

- `id` (Integer, Primary Key)
- `name` (String)
- `email` (String, Unique)

### Products Table

- `product_id` (Integer, Primary Key)
- `product_name` (String)
- `quantity` (Integer)
- `in_stock` (Boolean)

### Feedback Table

- `id` (Integer, Primary Key)
- `name` (String)
- `comment` (String)

## 📁 Project Structure

```
fastapi-neon-demo/
├── main.py          # FastAPI application and API endpoints
├── models.py        # SQLAlchemy database models
├── db.py           # Database configuration and connection
├── setup.py        # Database initialization script
├── .env            # Environment variables (not in repo)
├── .env.example    # Environment variables template
├── .gitignore      # Git ignore rules
└── README.md       # Project documentation
```

## 🔒 Environment Variables

Copy `.env.example` to `.env` and update with your values:

```env
DATABASE_URL="postgresql://username:password@host:port/database_name?sslmode=require"
```

## 🧪 Development

### Code Structure

- **main.py**: Contains the FastAPI app, Pydantic models, and API endpoints
- **models.py**: SQLAlchemy ORM models for database tables
- **db.py**: Database configuration and session management
- **setup.py**: Script to create database tables

### Adding New Features

1. Define new SQLAlchemy models in `models.py`
2. Create corresponding Pydantic models in `main.py`
3. Add API endpoints in `main.py`
4. Update database schema by running `setup.py`

## 🐛 Troubleshooting

### Common Issues

1. **Database Connection Error**:

   - Verify your DATABASE_URL in `.env`
   - Check NeonDB connection status
   - Ensure database exists

2. **Module Import Errors**:

   - Activate virtual environment
   - Install all dependencies: `pip install -r requirements.txt`

3. **Table Does Not Exist**:
   - Run `python setup.py` to create tables

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin feature-name`
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🔗 Resources

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [NeonDB Documentation](https://neon.tech/docs)
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/)
- [Pydantic Documentation](https://pydantic-docs.helpmanual.io/)

**Built with ❤️ using FastAPI and NeonDB**
