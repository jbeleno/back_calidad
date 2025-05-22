# back_calidad

This repository contains a microservices architecture for managing companies, users, and evaluation forms. Each microservice is developed in Python using FastAPI and SQLAlchemy, and connects to a PostgreSQL database.

## Microservices

- **evaluation-service**: Microservice for managing companies and users, with CRUD endpoints and basic authentication.
- **forms-management-service**: Microservice for managing forms, objectives, participants, and methodologies.
- **users-companies-service**: Microservice for managing companies and users, similar to evaluation-service but decoupled for scalability.

## Project Structure

```
back_calidad/
├── evaluation-service/
├── forms-management-service/
├── users-companies-service/
```

Each microservice contains its own `README.md` with specific instructions.

## General Requirements
- Python 3.10+
- PostgreSQL
- FastAPI
- SQLAlchemy
- Pydantic

## Execution
Each microservice can be run independently. See each microservice's README for installation and execution details.

---

# Español

Este repositorio contiene una arquitectura de microservicios para la gestión de empresas, usuarios y formularios de evaluación. Cada microservicio está desarrollado en Python usando FastAPI y SQLAlchemy, y se conecta a una base de datos PostgreSQL.

Consulta el README de cada microservicio para más detalles e instrucciones.