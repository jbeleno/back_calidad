# forms-management-service

Microservicio para la gestión de formularios, objetivos, participantes y metodologías.

## Descripción
Permite crear, leer, actualizar y eliminar formularios, objetivos, participantes y metodologías. Utiliza FastAPI, SQLAlchemy y Pydantic.

## Estructura principal
- `app/main.py`: Endpoints de la API.
- `app/models.py`: Modelos ORM.
- `app/schemas.py`: Esquemas de validación.
- `app/crud.py`: Lógica CRUD.
- `app/database.py`: Conexión a la base de datos.

## Instalación y ejecución
1. Instala dependencias:
   ```bash
   pip install -r requirements.txt
   ```
2. Ejecuta el microservicio:
   ```bash
   uvicorn app.main:app --reload
   ```

## Variables importantes
- `DATABASE_URL`: Cadena de conexión a PostgreSQL.

---

# English

Microservice for managing forms, objectives, participants, and methodologies. Provides CRUD operations. See code comments for details.