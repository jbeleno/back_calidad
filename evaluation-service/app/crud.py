# Name in es: Importación de Session
# Explanation: Imports Session from SQLAlchemy ORM to manage database sessions.
# Nombre en es: Importación de Session
# Explicación: Importa Session del ORM de SQLAlchemy para gestionar sesiones de base de datos.
from sqlalchemy.orm import Session
# Name in es: Importación de modelos y esquemas
# Explanation: Imports models and schemas from the current package for use in CRUD operations.
# Nombre en es: Importación de modelos y esquemas
# Explicación: Importa modelos y esquemas del paquete actual para usarlos en operaciones CRUD.
from . import models, schemas

# Name in es: get_empresas
# Explanation: Retrieves a list of companies from the database with optional pagination.
# Nombre en es: get_empresas
# Explicación: Recupera una lista de empresas de la base de datos con paginación opcional.
def get_empresas(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Empresa).offset(skip).limit(limit).all()

# Name in es: get_empresa
# Explanation: Retrieves a single company by its ID from the database.
# Nombre en es: get_empresa
# Explicación: Recupera una sola empresa por su ID de la base de datos.
def get_empresa(db: Session, empresa_id: int):
    return db.query(models.Empresa).filter(models.Empresa.id_empresa == empresa_id).first()

# Name in es: create_empresa
# Explanation: Creates a new company in the database using the provided schema.
# Nombre en es: create_empresa
# Explicación: Crea una nueva empresa en la base de datos usando el esquema proporcionado.
def create_empresa(db: Session, empresa: schemas.EmpresaCreate):
    db_empresa = models.Empresa(nombre=empresa.nombre, telefono=empresa.telefono)
    db.add(db_empresa)
    db.commit()
    db.refresh(db_empresa)
    return db_empresa

# Name in es: delete_empresa
# Explanation: Deletes a company from the database by its ID.
# Nombre en es: delete_empresa
# Explicación: Elimina una empresa de la base de datos por su ID.
def delete_empresa(db: Session, empresa_id: int):
    empresa = db.query(models.Empresa).filter(models.Empresa.id_empresa == empresa_id).first()
    if empresa:
        db.delete(empresa)
        db.commit()
    return empresa

# Name in es: update_empresa
# Explanation: Updates the information of a company in the database by its ID.
# Nombre en es: update_empresa
# Explicación: Actualiza la información de una empresa en la base de datos por su ID.
def update_empresa(db: Session, empresa_id: int, empresa_update: schemas.EmpresaCreate):
    empresa = db.query(models.Empresa).filter(models.Empresa.id_empresa == empresa_id).first()
    if empresa:
        empresa.nombre = empresa_update.nombre
        empresa.telefono = empresa_update.telefono
        db.commit()
        db.refresh(empresa)
    return empresa

# Name in es: Sección de Usuarios
# Explanation: Functions for user CRUD operations.
# Nombre en es: Sección de Usuarios
# Explicación: Funciones para operaciones CRUD de usuarios.

# Name in es: get_usuarios
# Explanation: Retrieves a list of users from the database with optional pagination.
# Nombre en es: get_usuarios
# Explicación: Recupera una lista de usuarios de la base de datos con paginación opcional.
def get_usuarios(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Usuario).offset(skip).limit(limit).all()

# Name in es: get_usuario
# Explanation: Retrieves a single user by their ID from the database.
# Nombre en es: get_usuario
# Explicación: Recupera un solo usuario por su ID de la base de datos.
def get_usuario(db: Session, usuario_id: int):
    return db.query(models.Usuario).filter(models.Usuario.id_usuario == usuario_id).first()

# Name in es: create_usuario
# Explanation: Creates a new user in the database using the provided schema.
# Nombre en es: create_usuario
# Explicación: Crea un nuevo usuario en la base de datos usando el esquema proporcionado.
def create_usuario(db: Session, usuario: schemas.UsuarioCreate):
    db_usuario = models.Usuario(**usuario.dict())
    db.add(db_usuario)
    db.commit()
    db.refresh(db_usuario)
    return db_usuario

# Name in es: update_usuario
# Explanation: Updates the information of a user in the database by their ID.
# Nombre en es: update_usuario
# Explicación: Actualiza la información de un usuario en la base de datos por su ID.
def update_usuario(db: Session, usuario_id: int, usuario_update: schemas.UsuarioCreate):
    usuario = db.query(models.Usuario).filter(models.Usuario.id_usuario == usuario_id).first()
    if usuario:
        for key, value in usuario_update.dict().items():
            setattr(usuario, key, value)
        db.commit()
        db.refresh(usuario)
    return usuario

# Name in es: delete_usuario
# Explanation: Deletes a user from the database by their ID.
# Nombre en es: delete_usuario
# Explicación: Elimina un usuario de la base de datos por su ID.
def delete_usuario(db: Session, usuario_id: int):
    usuario = db.query(models.Usuario).filter(models.Usuario.id_usuario == usuario_id).first()
    if usuario:
        db.delete(usuario)
        db.commit()
    return usuario

# Name in es: autenticar_usuario
# Explanation: Authenticates a user by their email and password.
# Nombre en es: autenticar_usuario
# Explicación: Autentica a un usuario por su correo y contraseña.
def autenticar_usuario(db: Session, correo: str, contraseña: str):
    return db.query(models.Usuario).filter(models.Usuario.correo == correo, models.Usuario.contraseña == contraseña).first()
