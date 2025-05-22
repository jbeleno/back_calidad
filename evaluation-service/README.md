# evaluation-service

Microservice for managing companies and users.

## Description
Allows you to create, read, update, and delete companies and users, as well as basic authentication. Uses FastAPI, SQLAlchemy, and Pydantic.

## Main Structure
- `app/main.py`: API endpoints.
- `app/models.py`: ORM models.
- `app/schemas.py`: Validation schemas.
- `app/crud.py`: CRUD logic.
- `app/database.py`: Database connection.

## Installation and Execution
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Run the microservice:
   ```bash
   uvicorn app.main:app --reload
   ```

## Important Variables
- `DATABASE_URL`: PostgreSQL connection string.

---

# Español

Microservicio para la gestión de empresas y usuarios. Permite crear, leer, actualizar y eliminar empresas y usuarios, así como autenticación básica. Utiliza FastAPI, SQLAlchemy y Pydantic. Consulta los comentarios en el código para más detalles.

