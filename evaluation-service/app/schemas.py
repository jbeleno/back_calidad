# Name in es: Importación de BaseModel
# Explanation: Imports BaseModel from Pydantic to define data validation and serialization schemas.
# Nombre en es: Importación de BaseModel
# Explicación: Importa BaseModel de Pydantic para definir esquemas de validación y serialización de datos.
from pydantic import BaseModel

# Name in es: EmpresaBase
# Explanation: Base schema for company data, used as a parent for other company schemas.
# Nombre en es: EmpresaBase
# Explicación: Esquema base para datos de empresa, usado como padre para otros esquemas de empresa.
class EmpresaBase(BaseModel):
    # Name in es: nombre
    # Explanation: Name of the company.
    # Nombre en es: nombre
    # Explicación: Nombre de la empresa.
    nombre: str
    # Name in es: telefono
    # Explanation: Phone number of the company, optional.
    # Nombre en es: telefono
    # Explicación: Número de teléfono de la empresa, opcional.
    telefono: str | None = None

# Name in es: EmpresaCreate
# Explanation: Schema for creating a new company, inherits from EmpresaBase.
# Nombre en es: EmpresaCreate
# Explicación: Esquema para crear una nueva empresa, hereda de EmpresaBase.
class EmpresaCreate(EmpresaBase):
    pass

# Name in es: Empresa
# Explanation: Schema representing a company with its ID, used for responses.
# Nombre en es: Empresa
# Explicación: Esquema que representa una empresa con su ID, usado para respuestas.
class Empresa(EmpresaBase):
    # Name in es: id_empresa
    # Explanation: Unique identifier of the company.
    # Nombre en es: id_empresa
    # Explicación: Identificador único de la empresa.
    id_empresa: int

    # Name in es: Config
    # Explanation: Enables ORM mode for compatibility with ORM objects.
    # Nombre en es: Config
    # Explicación: Habilita el modo ORM para compatibilidad con objetos ORM.
    class Config:
        orm_mode = True

# Name in es: UsuarioBase
# Explanation: Base schema for user data, used as a parent for other user schemas.
# Nombre en es: UsuarioBase
# Explicación: Esquema base para datos de usuario, usado como padre para otros esquemas de usuario.
class UsuarioBase(BaseModel):
    # Name in es: correo
    # Explanation: User's email address.
    # Nombre en es: correo
    # Explicación: Correo electrónico del usuario.
    correo: str
    # Name in es: contraseña
    # Explanation: User's password.
    # Nombre en es: contraseña
    # Explicación: Contraseña del usuario.
    contraseña: str
    # Name in es: nombre
    # Explanation: Name of the user.
    # Nombre en es: nombre
    # Explicación: Nombre del usuario.
    nombre: str
    # Name in es: rol
    # Explanation: Role of the user, default is 'usuario'.
    # Nombre en es: rol
    # Explicación: Rol del usuario, por defecto es 'usuario'.
    rol: str = 'usuario'

# Name in es: UsuarioCreate
# Explanation: Schema for creating a new user, inherits from UsuarioBase.
# Nombre en es: UsuarioCreate
# Explicación: Esquema para crear un nuevo usuario, hereda de UsuarioBase.
class UsuarioCreate(UsuarioBase):
    pass

# Name in es: Usuario
# Explanation: Schema representing a user with its ID, used for responses.
# Nombre en es: Usuario
# Explicación: Esquema que representa un usuario con su ID, usado para respuestas.
class Usuario(UsuarioBase):
    # Name in es: id_usuario
    # Explanation: Unique identifier of the user.
    # Nombre en es: id_usuario
    # Explicación: Identificador único del usuario.
    id_usuario: int
    # Name in es: Config
    # Explanation: Enables ORM mode for compatibility with ORM objects.
    # Nombre en es: Config
    # Explicación: Habilita el modo ORM para compatibilidad con objetos ORM.
    class Config:
        orm_mode = True

# Name in es: LoginRequest
# Explanation: Schema for user login requests, contains email and password.
# Nombre en es: LoginRequest
# Explicación: Esquema para solicitudes de inicio de sesión de usuario, contiene correo y contraseña.
class LoginRequest(BaseModel):
    # Name in es: correo
    # Explanation: User's email address for login.
    # Nombre en es: correo
    # Explicación: Correo electrónico del usuario para iniciar sesión.
    correo: str
    # Name in es: contraseña
    # Explanation: User's password for login.
    # Nombre en es: contraseña
    # Explicación: Contraseña del usuario para iniciar sesión.
    contraseña: str
