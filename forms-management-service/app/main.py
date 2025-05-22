# Name in es: Importaciones principales
# Explanation: Imports FastAPI, dependencies, exceptions, CORS middleware, and SQLAlchemy session management for the API.
# Nombre en es: Importaciones principales
# Explicación: Importa FastAPI, dependencias, excepciones, middleware CORS y gestión de sesión de SQLAlchemy para la API.
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from .database import engine, SessionLocal
from .models import Base
from . import crud, schemas
from fastapi.middleware.cors import CORSMiddleware

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
       allow_origins=["*"],  # O ["*"] solo para pruebas
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
    return {"msg": "Microservicio de Formularios funcionando"}

# Name in es: Crear formulario
# Explanation: Endpoint to create a new form.
# Nombre en es: Crear formulario
# Explicación: Endpoint para crear un nuevo formulario.
@app.post("/formularios/", response_model=schemas.Formulario, tags=["formularios"])
def create_formulario(formulario: schemas.FormularioCreate, db: Session = Depends(get_db)):
    return crud.create_formulario(db, formulario)

# Name in es: Leer formularios
# Explanation: Endpoint to get a list of forms with pagination.
# Nombre en es: Leer formularios
# Explicación: Endpoint para obtener una lista de formularios con paginación.
@app.get("/formularios/", response_model=list[schemas.Formulario], tags=["formularios"])
def read_formularios(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_formularios(db, skip=skip, limit=limit)

# Name in es: Leer formulario por ID
# Explanation: Endpoint to get a form by its ID.
# Nombre en es: Leer formulario por ID
# Explicación: Endpoint para obtener un formulario por su ID.
@app.get("/formularios/{formulario_id}", response_model=schemas.Formulario, tags=["formularios"])
def read_formulario(formulario_id: int, db: Session = Depends(get_db)):
    db_formulario = crud.get_formulario(db, formulario_id=formulario_id)
    if db_formulario is None:
        raise HTTPException(status_code=404, detail="Formulario no encontrado")
    return db_formulario

# Name in es: Actualizar formulario
# Explanation: Endpoint to update a form's information by its ID.
# Nombre en es: Actualizar formulario
# Explicación: Endpoint para actualizar la información de un formulario por su ID.
@app.put("/formularios/{formulario_id}", response_model=schemas.Formulario, tags=["formularios"])
def update_formulario(formulario_id: int, formulario: schemas.FormularioCreate, db: Session = Depends(get_db)):
    db_formulario = crud.update_formulario(db, formulario_id, formulario)
    if db_formulario is None:
        raise HTTPException(status_code=404, detail="Formulario no encontrado")
    return db_formulario

# Name in es: Eliminar formulario
# Explanation: Endpoint to delete a form by its ID.
# Nombre en es: Eliminar formulario
# Explicación: Endpoint para eliminar un formulario por su ID.
@app.delete("/formularios/{formulario_id}", response_model=schemas.Formulario, tags=["formularios"])
def delete_formulario(formulario_id: int, db: Session = Depends(get_db)):
    db_formulario = crud.delete_formulario(db, formulario_id)
    if db_formulario is None:
        raise HTTPException(status_code=404, detail="Formulario no encontrado")
    return db_formulario

# Name in es: Crear objetivo
# Explanation: Endpoint to create a new objective.
# Nombre en es: Crear objetivo
# Explicación: Endpoint para crear un nuevo objetivo.
@app.post("/objetivos/", response_model=schemas.ObjetivoFormulario, tags=["objetivos"])
def create_objetivo(objetivo: schemas.ObjetivoFormularioCreate, db: Session = Depends(get_db)):
    return crud.create_objetivo(db, objetivo)

# Name in es: Leer objetivos
# Explanation: Endpoint to get a list of objectives with pagination.
# Nombre en es: Leer objetivos
# Explicación: Endpoint para obtener una lista de objetivos con paginación.
@app.get("/objetivos/", response_model=list[schemas.ObjetivoFormulario], tags=["objetivos"])
def read_objetivos(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_objetivos(db, skip=skip, limit=limit)

# Name in es: Leer objetivo por ID
# Explanation: Endpoint to get an objective by its ID.
# Nombre en es: Leer objetivo por ID
# Explicación: Endpoint para obtener un objetivo por su ID.
@app.get("/objetivos/{objetivo_id}", response_model=schemas.ObjetivoFormulario, tags=["objetivos"])
def read_objetivo(objetivo_id: int, db: Session = Depends(get_db)):
    db_objetivo = crud.get_objetivo(db, objetivo_id=objetivo_id)
    if db_objetivo is None:
        raise HTTPException(status_code=404, detail="Objetivo no encontrado")
    return db_objetivo

# Name in es: Actualizar objetivo
# Explanation: Endpoint to update an objective's information by its ID.
# Nombre en es: Actualizar objetivo
# Explicación: Endpoint para actualizar la información de un objetivo por su ID.
@app.put("/objetivos/{objetivo_id}", response_model=schemas.ObjetivoFormulario, tags=["objetivos"])
def update_objetivo(objetivo_id: int, objetivo: schemas.ObjetivoFormularioCreate, db: Session = Depends(get_db)):
    db_objetivo = crud.update_objetivo(db, objetivo_id, objetivo)
    if db_objetivo is None:
        raise HTTPException(status_code=404, detail="Objetivo no encontrado")
    return db_objetivo

# Name in es: Eliminar objetivo
# Explanation: Endpoint to delete an objective by its ID.
# Nombre en es: Eliminar objetivo
# Explicación: Endpoint para eliminar un objetivo por su ID.
@app.delete("/objetivos/{objetivo_id}", response_model=schemas.ObjetivoFormulario, tags=["objetivos"])
def delete_objetivo(objetivo_id: int, db: Session = Depends(get_db)):
    db_objetivo = crud.delete_objetivo(db, objetivo_id)
    if db_objetivo is None:
        raise HTTPException(status_code=404, detail="Objetivo no encontrado")
    return db_objetivo

# Name in es: Crear participante
# Explanation: Endpoint to create a new participant.
# Nombre en es: Crear participante
# Explicación: Endpoint para crear un nuevo participante.
@app.post("/participantes/", response_model=schemas.ParticipanteFormulario, tags=["participantes"])
def create_participante(participante: schemas.ParticipanteFormularioCreate, db: Session = Depends(get_db)):
    return crud.create_participante(db, participante)

# Name in es: Leer participantes
# Explanation: Endpoint to get a list of participants with pagination.
# Nombre en es: Leer participantes
# Explicación: Endpoint para obtener una lista de participantes con paginación.
@app.get("/participantes/", response_model=list[schemas.ParticipanteFormulario], tags=["participantes"])
def read_participantes(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_participantes(db, skip=skip, limit=limit)

# Name in es: Leer participante por ID
# Explanation: Endpoint to get a participant by their ID.
# Nombre en es: Leer participante por ID
# Explicación: Endpoint para obtener un participante por su ID.
@app.get("/participantes/{participante_id}", response_model=schemas.ParticipanteFormulario, tags=["participantes"])
def read_participante(participante_id: int, db: Session = Depends(get_db)):
    db_participante = crud.get_participante(db, participante_id=participante_id)
    if db_participante is None:
        raise HTTPException(status_code=404, detail="Participante no encontrado")
    return db_participante

# Name in es: Actualizar participante
# Explanation: Endpoint to update a participant's information by their ID.
# Nombre en es: Actualizar participante
# Explicación: Endpoint para actualizar la información de un participante por su ID.
@app.put("/participantes/{participante_id}", response_model=schemas.ParticipanteFormulario, tags=["participantes"])
def update_participante(participante_id: int, participante: schemas.ParticipanteFormularioCreate, db: Session = Depends(get_db)):
    db_participante = crud.update_participante(db, participante_id, participante)
    if db_participante is None:
        raise HTTPException(status_code=404, detail="Participante no encontrado")
    return db_participante

# Name in es: Eliminar participante
# Explanation: Endpoint to delete a participant by their ID.
# Nombre en es: Eliminar participante
# Explicación: Endpoint para eliminar un participante por su ID.
@app.delete("/participantes/{participante_id}", response_model=schemas.ParticipanteFormulario, tags=["participantes"])
def delete_participante(participante_id: int, db: Session = Depends(get_db)):
    db_participante = crud.delete_participante(db, participante_id)
    if db_participante is None:
        raise HTTPException(status_code=404, detail="Participante no encontrado")
    return db_participante

# Name in es: Crear metodología
# Explanation: Endpoint to create a new methodology.
# Nombre en es: Crear metodología
# Explicación: Endpoint para crear una nueva metodología.
@app.post("/metodologias/", response_model=schemas.Metodologia, tags=["metodologias"])
def create_metodologia(metodologia: schemas.MetodologiaCreate, db: Session = Depends(get_db)):
    return crud.create_metodologia(db, metodologia)

# Name in es: Leer metodologías
# Explanation: Endpoint to get a list of methodologies with pagination.
# Nombre en es: Leer metodologías
# Explicación: Endpoint para obtener una lista de metodologías con paginación.
@app.get("/metodologias/", response_model=list[schemas.Metodologia], tags=["metodologias"])
def read_metodologias(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_metodologias(db, skip=skip, limit=limit)

# Name in es: Leer metodología por ID
# Explanation: Endpoint to get a methodology by its ID.
# Nombre en es: Leer metodología por ID
# Explicación: Endpoint para obtener una metodología por su ID.
@app.get("/metodologias/{metodologia_id}", response_model=schemas.Metodologia, tags=["metodologias"])
def read_metodologia(metodologia_id: int, db: Session = Depends(get_db)):
    db_metodologia = crud.get_metodologia(db, metodologia_id=metodologia_id)
    if db_metodologia is None:
        raise HTTPException(status_code=404, detail="Metodología no encontrada")
    return db_metodologia

# Name in es: Actualizar metodología
# Explanation: Endpoint to update a methodology's information by its ID.
# Nombre en es: Actualizar metodología
# Explicación: Endpoint para actualizar la información de una metodología por su ID.
@app.put("/metodologias/{metodologia_id}", response_model=schemas.Metodologia, tags=["metodologias"])
def update_metodologia(metodologia_id: int, metodologia: schemas.MetodologiaCreate, db: Session = Depends(get_db)):
    db_metodologia = crud.update_metodologia(db, metodologia_id, metodologia)
    if db_metodologia is None:
        raise HTTPException(status_code=404, detail="Metodología no encontrada")
    return db_metodologia

# Name in es: Eliminar metodología
# Explanation: Endpoint to delete a methodology by its ID.
# Nombre en es: Eliminar metodología
# Explicación: Endpoint para eliminar una metodología por su ID.
@app.delete("/metodologias/{metodologia_id}", response_model=schemas.Metodologia, tags=["metodologias"])
def delete_metodologia(metodologia_id: int, db: Session = Depends(get_db)):
    db_metodologia = crud.delete_metodologia(db, metodologia_id)
    if db_metodologia is None:
        raise HTTPException(status_code=404, detail="Metodología no encontrada")
    return db_metodologia
