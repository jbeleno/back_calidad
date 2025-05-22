# Name in es: Importaciones de SQLAlchemy
# Explanation: These lines import the necessary classes from SQLAlchemy to define database models and columns.
# Nombre en es: Importaciones de SQLAlchemy
# Explicación: Estas líneas importan las clases necesarias de SQLAlchemy para definir modelos y columnas de la base de datos.
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Name in es: Base
# Explanation: This line creates a base class for all ORM models using SQLAlchemy's declarative system.
# Nombre en es: Base
# Explicación: Esta línea crea una clase base para todos los modelos ORM usando el sistema declarativo de SQLAlchemy.
Base = declarative_base()

# Name in es: Empresa
# Explanation: This class represents the 'empresas' table in the database, storing company information.
# Nombre en es: Empresa
# Explicación: Esta clase representa la tabla 'empresas' en la base de datos, almacenando información de la empresa.
class Empresa(Base):
    __tablename__ = "empresas"
    # Name in es: id_empresa
    # Explanation: Primary key of the company, unique identifier.
    # Nombre en es: id_empresa
    # Explicación: Clave primaria de la empresa, identificador único.
    id_empresa = Column(Integer, primary_key=True, index=True)
    # Name in es: nombre
    # Explanation: Name of the company, cannot be null.
    # Nombre en es: nombre
    # Explicación: Nombre de la empresa, no puede ser nulo.
    nombre = Column(String(255), nullable=False)
    # Name in es: telefono
    # Explanation: Phone number of the company.
    # Nombre en es: telefono
    # Explicación: Número de teléfono de la empresa.
    telefono = Column(String(50))

# Name in es: Usuario
# Explanation: This class represents the 'usuarios' table in the database, storing user information.
# Nombre en es: Usuario
# Explicación: Esta clase representa la tabla 'usuarios' en la base de datos, almacenando información del usuario.
class Usuario(Base):
    __tablename__ = "usuarios"
    # Name in es: id_usuario
    # Explanation: Primary key of the user, unique identifier.
    # Nombre en es: id_usuario
    # Explicación: Clave primaria del usuario, identificador único.
    id_usuario = Column(Integer, primary_key=True, index=True)
    # Name in es: correo
    # Explanation: User's email, must be unique and not null.
    # Nombre en es: correo
    # Explicación: Correo electrónico del usuario, debe ser único y no nulo.
    correo = Column(String(255), unique=True, nullable=False)
    # Name in es: contraseña
    # Explanation: User's password, cannot be null.
    # Nombre en es: contraseña
    # Explicación: Contraseña del usuario, no puede ser nula.
    contraseña = Column(String(255), nullable=False)
    # Name in es: nombre
    # Explanation: Name of the user, cannot be null.
    # Nombre en es: nombre
    # Explicación: Nombre del usuario, no puede ser nulo.
    nombre = Column(String(100), nullable=False)
    # Name in es: rol
    # Explanation: Role of the user, default is 'usuario'.
    # Nombre en es: rol
    # Explicación: Rol del usuario, por defecto es 'usuario'.
    rol = Column(String(50), nullable=False, default='usuario')
