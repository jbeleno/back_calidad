"""
Pydantic schemas for request and response validation.

Defines data validation and serialization for the main entities in the forms management service.
Dependencies: Pydantic.
"""
from pydantic import BaseModel
from datetime import date


class FormularioBase(BaseModel):
 
    id_empresa: int
    fecha: date
    ciudad: str | None = None
    nombre_software: str | None = None
    id_usuario: int
    id_metodologia: int

class FormularioCreate(FormularioBase):
    pass

class Formulario(FormularioBase):
    id_formulario: int
    class Config:
        orm_mode = True

class ObjetivoFormularioBase(BaseModel):
    id_formulario: int
    descripcion: str
    tipo: str

class ObjetivoFormularioCreate(ObjetivoFormularioBase):
    pass
    
class ObjetivoFormulario(ObjetivoFormularioBase):
    id_objetivo: int
    class Config:
        orm_mode = True

class ParticipanteFormularioBase(BaseModel):
    id_formulario: int
    cargo: str | None = None
    nombre: str | None = None
    firma: str | None = None

class ParticipanteFormularioCreate(ParticipanteFormularioBase):
    pass

class ParticipanteFormulario(ParticipanteFormularioBase):
    id_participante: int
    class Config:
        orm_mode = True

class MetodologiaBase(BaseModel):
    nombre: str
    descripcion: str | None = None

class MetodologiaCreate(MetodologiaBase):
    pass

class Metodologia(MetodologiaBase):
    id_metodologia: int
    class Config:
        orm_mode = True
