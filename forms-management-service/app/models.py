"""
SQLAlchemy ORM models for the application.

Defines the database schema for the main entities used in the forms management service.
Dependencies: SQLAlchemy.
"""
from sqlalchemy import Column, Integer, String, Date, Text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Formulario(Base):
    __tablename__ = "formulario"
    id_formulario = Column(Integer, primary_key=True, index=True)
    id_empresa = Column(Integer, nullable=False)
    fecha = Column(Date, nullable=False)
    ciudad = Column(String(100))
    nombre_software = Column(String(100))
    id_usuario = Column(Integer, nullable=False)
    id_metodologia = Column(Integer, nullable=False)

class ObjetivoFormulario(Base):
    __tablename__ = "objetivos_formulario"
    id_objetivo = Column(Integer, primary_key=True, index=True)
    id_formulario = Column(Integer, nullable=False)
    descripcion = Column(Text, nullable=False)
    tipo = Column(String(20)) 

class ParticipanteFormulario(Base):
    __tablename__ = "participantes_formulario"
    id_participante = Column(Integer, primary_key=True, index=True)
    id_formulario = Column(Integer, nullable=False)
    cargo = Column(String(100))
    nombre = Column(String(255))
    firma = Column(Text)

class Metodologia(Base):
    __tablename__ = "metodologias"
    id_metodologia = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    descripcion = Column(Text)