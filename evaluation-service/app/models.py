"""
SQLAlchemy ORM models for the application.

Defines the database schema for 'Empresa' and 'Usuario' entities.
Dependencies: SQLAlchemy.
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class Empresa(Base):
    __tablename__ = "empresas"
    id_empresa = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(255), nullable=False)
    telefono = Column(String(50))

class Usuario(Base):
    __tablename__ = "usuarios"
    id_usuario = Column(Integer, primary_key=True, index=True)
    correo = Column(String(255), unique=True, nullable=False)
    contraseña = Column(String(255), nullable=False)
    nombre = Column(String(100), nullable=False)
    rol = Column(String(50), nullable=False, default='usuario')
