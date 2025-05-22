# back_calidad

Este repositorio contiene una arquitectura de microservicios para la gestión de empresas, usuarios y formularios de evaluación. Cada microservicio está desarrollado en Python usando FastAPI y SQLAlchemy, y se conecta a una base de datos PostgreSQL.

## Microservicios

- **evaluation-service**: Microservicio para la gestión de empresas y usuarios, con endpoints CRUD y autenticación básica.
- **forms-management-service**: Microservicio para la gestión de formularios, objetivos, participantes y metodologías.
- **users-companies-service**: Microservicio para la gestión de empresas y usuarios, similar a evaluation-service pero desacoplado para escalabilidad.

## Estructura del proyecto

```
back_calidad/
├── evaluation-service/
├── forms-management-service/
├── users-companies-service/
```

Cada microservicio contiene su propio `README.md` con instrucciones específicas.

## Requisitos generales
- Python 3.10+
- PostgreSQL
- FastAPI
- SQLAlchemy
- Pydantic

## Ejecución
Cada microservicio puede ejecutarse de forma independiente. Consulta el README de cada uno para detalles de instalación y ejecución.

---

# English

This repository contains a microservices architecture for managing companies, users, and evaluation forms. Each microservice is developed in Python using FastAPI and SQLAlchemy, and connects to a PostgreSQL database.

See each microservice's README for more details and instructions.