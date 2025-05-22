# Name in es: Importaciones principales
# Explanation: Imports FastAPI, dependencies, exceptions, status codes, CORS middleware, and SQLAlchemy session management for the API.
# Nombre en es: Importaciones principales
# Explicación: Importa FastAPI, dependencias, excepciones, códigos de estado, middleware CORS y gestión de sesión de SQLAlchemy para la API.
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from .database import engine, SessionLocal
from .models import Base
from . import crud, schemas

# Name in es: Instancia de la aplicación FastAPI
# Explanation: Creates the FastAPI application instance.
# Nombre en es: Instancia de la aplicación FastAPI
# Explicación: Crea la instancia de la aplicación FastAPI.
app = FastAPI()

# Name in es: Configuración de CORS
# Explanation: Adds CORS middleware to allow cross-origin requests.
# Nombre en es: Configuración de CORS
# Explicación: Agrega el middleware CORS para permitir solicitudes de diferentes orígenes.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Puedes restringir a ["http://localhost:5173"] si lo prefieres
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Name in es: Evento de inicio
# Explanation: Creates all database tables at application startup.
# Nombre en es: Evento de inicio
# Explicación: Crea todas las tablas de la base de datos al iniciar la aplicación.
@app.on_event("startup")
def startup():
    Base.metadata.create_all(bind=engine)

# Name in es: Dependencia get_db
# Explanation: Dependency to get a database session for each request.
# Nombre en es: Dependencia get_db
# Explicación: Dependencia para obtener una sesión de base de datos por cada petición.
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Name in es: Endpoint raíz
# Explanation: Root endpoint to check if the service is running.
# Nombre en es: Endpoint raíz
# Explicación: Endpoint raíz para verificar si el servicio está funcionando.
@app.get("/", tags=["root"])
def read_root():
    return {"msg": "Microservicio de Empresas funcionando"}

# Name in es: Crear empresa
# Explanation: Endpoint to create a new company.
# Nombre en es: Crear empresa
# Explicación: Endpoint para crear una nueva empresa.
@app.post("/empresas/", response_model=schemas.Empresa, tags=["empresas"])
def create_empresa(empresa: schemas.EmpresaCreate, db: Session = Depends(get_db)):
    return crud.create_empresa(db, empresa)

# Name in es: Leer empresas
# Explanation: Endpoint to get a list of companies with pagination.
# Nombre en es: Leer empresas
# Explicación: Endpoint para obtener una lista de empresas con paginación.
@app.get("/empresas/", response_model=list[schemas.Empresa], tags=["empresas"])
def read_empresas(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_empresas(db, skip=skip, limit=limit)

# Name in es: Leer empresa por ID
# Explanation: Endpoint to get a company by its ID.
# Nombre en es: Leer empresa por ID
# Explicación: Endpoint para obtener una empresa por su ID.
@app.get("/empresas/{empresa_id}", response_model=schemas.Empresa, tags=["empresas"])
def read_empresa(empresa_id: int, db: Session = Depends(get_db)):
    db_empresa = crud.get_empresa(db, empresa_id=empresa_id)
    if db_empresa is None:
        raise HTTPException(status_code=404, detail="Empresa no encontrada")
    return db_empresa

# Name in es: Actualizar empresa
# Explanation: Endpoint to update a company's information by its ID.
# Nombre en es: Actualizar empresa
# Explicación: Endpoint para actualizar la información de una empresa por su ID.
@app.put("/empresas/{empresa_id}", response_model=schemas.Empresa, tags=["empresas"])
def update_empresa(empresa_id: int, empresa: schemas.EmpresaCreate, db: Session = Depends(get_db)):
    db_empresa = crud.update_empresa(db, empresa_id, empresa)
    if db_empresa is None:
        raise HTTPException(status_code=404, detail="Empresa no encontrada")
    return db_empresa

# Name in es: Eliminar empresa
# Explanation: Endpoint to delete a company by its ID.
# Nombre en es: Eliminar empresa
# Explicación: Endpoint para eliminar una empresa por su ID.
@app.delete("/empresas/{empresa_id}", response_model=schemas.Empresa, tags=["empresas"])
def delete_empresa(empresa_id: int, db: Session = Depends(get_db)):
    db_empresa = crud.delete_empresa(db, empresa_id)
    if db_empresa is None:
        raise HTTPException(status_code=404, detail="Empresa no encontrada")
    return db_empresa

# Name in es: Crear usuario
# Explanation: Endpoint to create a new user.
# Nombre en es: Crear usuario
# Explicación: Endpoint para crear un nuevo usuario.
@app.post("/usuarios/", response_model=schemas.Usuario, tags=["usuarios"])
def create_usuario(usuario: schemas.UsuarioCreate, db: Session = Depends(get_db)):
    return crud.create_usuario(db, usuario)

# Name in es: Leer usuarios
# Explanation: Endpoint to get a list of users with pagination.
# Nombre en es: Leer usuarios
# Explicación: Endpoint para obtener una lista de usuarios con paginación.
@app.get("/usuarios/", response_model=list[schemas.Usuario], tags=["usuarios"])
def read_usuarios(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_usuarios(db, skip=skip, limit=limit)

# Name in es: Leer usuario por ID
# Explanation: Endpoint to get a user by their ID.
# Nombre en es: Leer usuario por ID
# Explicación: Endpoint para obtener un usuario por su ID.
@app.get("/usuarios/{usuario_id}", response_model=schemas.Usuario, tags=["usuarios"])
def read_usuario(usuario_id: int, db: Session = Depends(get_db)):
    db_usuario = crud.get_usuario(db, usuario_id=usuario_id)
    if db_usuario is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return db_usuario

# Name in es: Actualizar usuario
# Explanation: Endpoint to update a user's information by their ID.
# Nombre en es: Actualizar usuario
# Explicación: Endpoint para actualizar la información de un usuario por su ID.
@app.put("/usuarios/{usuario_id}", response_model=schemas.Usuario, tags=["usuarios"])
def update_usuario(usuario_id: int, usuario: schemas.UsuarioCreate, db: Session = Depends(get_db)):
    db_usuario = crud.update_usuario(db, usuario_id, usuario)
    if db_usuario is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return db_usuario

# Name in es: Eliminar usuario
# Explanation: Endpoint to delete a user by their ID.
# Nombre en es: Eliminar usuario
# Explicación: Endpoint para eliminar un usuario por su ID.
@app.delete("/usuarios/{usuario_id}", response_model=schemas.Usuario, tags=["usuarios"])
def delete_usuario(usuario_id: int, db: Session = Depends(get_db)):
    db_usuario = crud.delete_usuario(db, usuario_id)
    if db_usuario is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return db_usuario

# Name in es: Login de usuario
# Explanation: Endpoint to authenticate a user with email and password.
# Nombre en es: Login de usuario
# Explicación: Endpoint para autenticar a un usuario con correo y contraseña.
@app.post("/login", response_model=schemas.Usuario, tags=["usuarios"])
def login(request: schemas.LoginRequest, db: Session = Depends(get_db)):
    usuario = crud.autenticar_usuario(db, request.correo, request.contraseña)
    if not usuario:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Correo o contraseña incorrectos")
    return usuario
