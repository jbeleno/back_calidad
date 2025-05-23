"""
Pydantic schemas for request and response validation.

Defines data validation and serialization for 'Empresa' and 'Usuario' entities.
Dependencies: Pydantic.
"""
from pydantic import BaseModel


class EmpresaBase(BaseModel):
    nombre: str
    telefono: str | None = None

class EmpresaCreate(EmpresaBase):
    pass

class Empresa(EmpresaBase):
    
    id_empresa: int
    class Config:
        orm_mode = True

class UsuarioBase(BaseModel):
    correo: str
    contraseña: str
    nombre: str
    rol: str = 'usuario'


class UsuarioCreate(UsuarioBase):
    pass

class Usuario(UsuarioBase):

    id_usuario: int
    class Config:
        orm_mode = True


class LoginRequest(BaseModel):
    correo: str
    contraseña: str
