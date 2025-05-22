from sqlalchemy.orm import Session
from . import models, schemas

# Name in es: get_formularios
# Explanation: Retrieves a list of forms from the database with optional pagination.
# Nombre en es: get_formularios
# Explicación: Recupera una lista de formularios de la base de datos con paginación opcional.
def get_formularios(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Formulario).offset(skip).limit(limit).all()

# Name in es: get_formulario
# Explanation: Retrieves a single form by its ID from the database.
# Nombre en es: get_formulario
# Explicación: Recupera un solo formulario por su ID de la base de datos.
def get_formulario(db: Session, formulario_id: int):
    return db.query(models.Formulario).filter(models.Formulario.id_formulario == formulario_id).first()

# Name in es: create_formulario
# Explanation: Creates a new form in the database using the provided schema.
# Nombre en es: create_formulario
# Explicación: Crea un nuevo formulario en la base de datos usando el esquema proporcionado.
def create_formulario(db: Session, formulario: schemas.FormularioCreate):
    db_formulario = models.Formulario(**formulario.dict())
    db.add(db_formulario)
    db.commit()
    db.refresh(db_formulario)
    return db_formulario

# Name in es: update_formulario
# Explanation: Updates the information of a form in the database by its ID.
# Nombre en es: update_formulario
# Explicación: Actualiza la información de un formulario en la base de datos por su ID.
def update_formulario(db: Session, formulario_id: int, formulario_update: schemas.FormularioCreate):
    formulario = db.query(models.Formulario).filter(models.Formulario.id_formulario == formulario_id).first()
    if formulario:
        for key, value in formulario_update.dict().items():
            setattr(formulario, key, value)
        db.commit()
        db.refresh(formulario)
    return formulario

# Name in es: delete_formulario
# Explanation: Deletes a form from the database by its ID.
# Nombre en es: delete_formulario
# Explicación: Elimina un formulario de la base de datos por su ID.
def delete_formulario(db: Session, formulario_id: int):
    formulario = db.query(models.Formulario).filter(models.Formulario.id_formulario == formulario_id).first()
    if formulario:
        db.delete(formulario)
        db.commit()
    return formulario

# Name in es: Sección de Objetivos
# Explanation: Functions for objectives CRUD operations.
# Nombre en es: Sección de Objetivos
# Explicación: Funciones para operaciones CRUD de objetivos.

# Name in es: get_objetivos
# Explanation: Retrieves a list of objectives from the database with optional pagination.
# Nombre en es: get_objetivos
# Explicación: Recupera una lista de objetivos de la base de datos con paginación opcional.
def get_objetivos(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.ObjetivoFormulario).offset(skip).limit(limit).all()

# Name in es: get_objetivo
# Explanation: Retrieves a single objective by its ID from the database.
# Nombre en es: get_objetivo
# Explicación: Recupera un solo objetivo por su ID de la base de datos.
def get_objetivo(db: Session, objetivo_id: int):
    return db.query(models.ObjetivoFormulario).filter(models.ObjetivoFormulario.id_objetivo == objetivo_id).first()

# Name in es: create_objetivo
# Explanation: Creates a new objective in the database using the provided schema.
# Nombre en es: create_objetivo
# Explicación: Crea un nuevo objetivo en la base de datos usando el esquema proporcionado.
def create_objetivo(db: Session, objetivo: schemas.ObjetivoFormularioCreate):
    db_objetivo = models.ObjetivoFormulario(**objetivo.dict())
    db.add(db_objetivo)
    db.commit()
    db.refresh(db_objetivo)
    return db_objetivo

# Name in es: update_objetivo
# Explanation: Updates the information of an objective in the database by its ID.
# Nombre en es: update_objetivo
# Explicación: Actualiza la información de un objetivo en la base de datos por su ID.
def update_objetivo(db: Session, objetivo_id: int, objetivo_update: schemas.ObjetivoFormularioCreate):
    objetivo = db.query(models.ObjetivoFormulario).filter(models.ObjetivoFormulario.id_objetivo == objetivo_id).first()
    if objetivo:
        for key, value in objetivo_update.dict().items():
            setattr(objetivo, key, value)
        db.commit()
        db.refresh(objetivo)
    return objetivo

# Name in es: delete_objetivo
# Explanation: Deletes an objective from the database by its ID.
# Nombre en es: delete_objetivo
# Explicación: Elimina un objetivo de la base de datos por su ID.
def delete_objetivo(db: Session, objetivo_id: int):
    objetivo = db.query(models.ObjetivoFormulario).filter(models.ObjetivoFormulario.id_objetivo == objetivo_id).first()
    if objetivo:
        db.delete(objetivo)
        db.commit()
    return objetivo

# Name in es: Sección de Participantes
# Explanation: Functions for participants CRUD operations.
# Nombre en es: Sección de Participantes
# Explicación: Funciones para operaciones CRUD de participantes.

# Name in es: get_participantes
# Explanation: Retrieves a list of participants from the database with optional pagination.
# Nombre en es: get_participantes
# Explicación: Recupera una lista de participantes de la base de datos con paginación opcional.
def get_participantes(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.ParticipanteFormulario).offset(skip).limit(limit).all()

# Name in es: get_participante
# Explanation: Retrieves a single participant by their ID from the database.
# Nombre en es: get_participante
# Explicación: Recupera un solo participante por su ID de la base de datos.
def get_participante(db: Session, participante_id: int):
    return db.query(models.ParticipanteFormulario).filter(models.ParticipanteFormulario.id_participante == participante_id).first()

# Name in es: create_participante
# Explanation: Creates a new participant in the database using the provided schema.
# Nombre en es: create_participante
# Explicación: Crea un nuevo participante en la base de datos usando el esquema proporcionado.
def create_participante(db: Session, participante: schemas.ParticipanteFormularioCreate):
    db_participante = models.ParticipanteFormulario(**participante.dict())
    db.add(db_participante)
    db.commit()
    db.refresh(db_participante)
    return db_participante

# Name in es: update_participante
# Explanation: Updates the information of a participant in the database by their ID.
# Nombre en es: update_participante
# Explicación: Actualiza la información de un participante en la base de datos por su ID.
def update_participante(db: Session, participante_id: int, participante_update: schemas.ParticipanteFormularioCreate):
    participante = db.query(models.ParticipanteFormulario).filter(models.ParticipanteFormulario.id_participante == participante_id).first()
    if participante:
        for key, value in participante_update.dict().items():
            setattr(participante, key, value)
        db.commit()
        db.refresh(participante)
    return participante

# Name in es: delete_participante
# Explanation: Deletes a participant from the database by their ID.
# Nombre en es: delete_participante
# Explicación: Elimina un participante de la base de datos por su ID.
def delete_participante(db: Session, participante_id: int):
    participante = db.query(models.ParticipanteFormulario).filter(models.ParticipanteFormulario.id_participante == participante_id).first()
    if participante:
        db.delete(participante)
        db.commit()
    return participante

# Name in es: Sección de Metodologías
# Explanation: Functions for methodologies CRUD operations.
# Nombre en es: Sección de Metodologías
# Explicación: Funciones para operaciones CRUD de metodologías.

# Name in es: get_metodologias
# Explanation: Retrieves a list of methodologies from the database with optional pagination.
# Nombre en es: get_metodologias
# Explicación: Recupera una lista de metodologías de la base de datos con paginación opcional.
def get_metodologias(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Metodologia).offset(skip).limit(limit).all()

# Name in es: get_metodologia
# Explanation: Retrieves a single methodology by its ID from the database.
# Nombre en es: get_metodologia
# Explicación: Recupera una sola metodología por su ID de la base de datos.
def get_metodologia(db: Session, metodologia_id: int):
    return db.query(models.Metodologia).filter(models.Metodologia.id_metodologia == metodologia_id).first()

# Name in es: create_metodologia
# Explanation: Creates a new methodology in the database using the provided schema.
# Nombre en es: create_metodologia
# Explicación: Crea una nueva metodología en la base de datos usando el esquema proporcionado.
def create_metodologia(db: Session, metodologia: schemas.MetodologiaCreate):
    db_metodologia = models.Metodologia(**metodologia.dict())
    db.add(db_metodologia)
    db.commit()
    db.refresh(db_metodologia)
    return db_metodologia

# Name in es: update_metodologia
# Explanation: Updates the information of a methodology in the database by its ID.
# Nombre en es: update_metodologia
# Explicación: Actualiza la información de una metodología en la base de datos por su ID.
def update_metodologia(db: Session, metodologia_id: int, metodologia_update: schemas.MetodologiaCreate):
    metodologia = db.query(models.Metodologia).filter(models.Metodologia.id_metodologia == metodologia_id).first()
    if metodologia:
        for key, value in metodologia_update.dict().items():
            setattr(metodologia, key, value)
        db.commit()
        db.refresh(metodologia)
    return metodologia

# Name in es: delete_metodologia
# Explanation: Deletes a methodology from the database by its ID.
# Nombre en es: delete_metodologia
# Explicación: Elimina una metodología de la base de datos por su ID.
def delete_metodologia(db: Session, metodologia_id: int):
    metodologia = db.query(models.Metodologia).filter(models.Metodologia.id_metodologia == metodologia_id).first()
    if metodologia:
        db.delete(metodologia)
        db.commit()
    return metodologia
