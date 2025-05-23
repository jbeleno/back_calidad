from sqlalchemy.orm import Session
from . import models, schemas

"""
CRUD operations for database entities.

Implements create, read, update, and delete logic for the main entities in the users-companies service.
Dependencies: SQLAlchemy ORM, application models and schemas.
"""


def get_empresas(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Empresa).offset(skip).limit(limit).all()


def get_empresa(db: Session, empresa_id: int):
    return db.query(models.Empresa).filter(models.Empresa.id_empresa == empresa_id).first()


def create_empresa(db: Session, empresa: schemas.EmpresaCreate):
    db_empresa = models.Empresa(nombre=empresa.nombre, telefono=empresa.telefono)
    db.add(db_empresa)
    db.commit()
    db.refresh(db_empresa)
    return db_empresa


def delete_empresa(db: Session, empresa_id: int):
    empresa = db.query(models.Empresa).filter(models.Empresa.id_empresa == empresa_id).first()
    if empresa:
        db.delete(empresa)
        db.commit()
    return empresa


def update_empresa(db: Session, empresa_id: int, empresa_update: schemas.EmpresaCreate):
    empresa = db.query(models.Empresa).filter(models.Empresa.id_empresa == empresa_id).first()
    if empresa:
        empresa.nombre = empresa_update.nombre
        empresa.telefono = empresa_update.telefono
        db.commit()
        db.refresh(empresa)
    return empresa


def get_usuarios(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Usuario).offset(skip).limit(limit).all()

def get_usuario(db: Session, usuario_id: int):
    return db.query(models.Usuario).filter(models.Usuario.id_usuario == usuario_id).first()


def create_usuario(db: Session, usuario: schemas.UsuarioCreate):
    db_usuario = models.Usuario(**usuario.dict())
    db.add(db_usuario)
    db.commit()
    db.refresh(db_usuario)
    return db_usuario

def update_usuario(db: Session, usuario_id: int, usuario_update: schemas.UsuarioCreate):
    usuario = db.query(models.Usuario).filter(models.Usuario.id_usuario == usuario_id).first()
    if usuario:
        for key, value in usuario_update.dict().items():
            setattr(usuario, key, value)
        db.commit()
        db.refresh(usuario)
    return usuario

def delete_usuario(db: Session, usuario_id: int):
    usuario = db.query(models.Usuario).filter(models.Usuario.id_usuario == usuario_id).first()
    if usuario:
        db.delete(usuario)
        db.commit()
    return usuario

def autenticar_usuario(db: Session, correo: str, contraseña: str):
    return db.query(models.Usuario).filter(models.Usuario.correo == correo, models.Usuario.contraseña == contraseña).first()
