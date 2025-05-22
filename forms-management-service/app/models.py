# Name in es: Importaciones de SQLAlchemy
# Explanation: These lines import the necessary classes from SQLAlchemy to define database models and columns.
# Nombre en es: Importaciones de SQLAlchemy
# Explicación: Estas líneas importan las clases necesarias de SQLAlchemy para definir modelos y columnas de la base de datos.
from sqlalchemy import Column, Integer, String, Date, Text
from sqlalchemy.ext.declarative import declarative_base

# Name in es: Base
# Explanation: This line creates a base class for all ORM models using SQLAlchemy's declarative system.
# Nombre en es: Base
# Explicación: Esta línea crea una clase base para todos los modelos ORM usando el sistema declarativo de SQLAlchemy.
Base = declarative_base()

# Name in es: Formulario
# Explanation: This class represents the 'formulario' table in the database, storing form information.
# Nombre en es: Formulario
# Explicación: Esta clase representa la tabla 'formulario' en la base de datos, almacenando información de formularios.
class Formulario(Base):
    __tablename__ = "formulario"
    # Name in es: id_formulario
    # Explanation: Primary key of the form, unique identifier.
    # Nombre en es: id_formulario
    # Explicación: Clave primaria del formulario, identificador único.
    id_formulario = Column(Integer, primary_key=True, index=True)
    # Name in es: id_empresa
    # Explanation: Foreign key referencing the company.
    # Nombre en es: id_empresa
    # Explicación: Llave foránea que referencia la empresa.
    id_empresa = Column(Integer, nullable=False)
    # Name in es: fecha
    # Explanation: Date of the form.
    # Nombre en es: fecha
    # Explicación: Fecha del formulario.
    fecha = Column(Date, nullable=False)
    # Name in es: ciudad
    # Explanation: City where the form was filled.
    # Nombre en es: ciudad
    # Explicación: Ciudad donde se llenó el formulario.
    ciudad = Column(String(100))
    # Name in es: nombre_software
    # Explanation: Name of the software evaluated in the form.
    # Nombre en es: nombre_software
    # Explicación: Nombre del software evaluado en el formulario.
    nombre_software = Column(String(100))
    # Name in es: id_usuario
    # Explanation: Foreign key referencing the user.
    # Nombre en es: id_usuario
    # Explicación: Llave foránea que referencia al usuario.
    id_usuario = Column(Integer, nullable=False)
    # Name in es: id_metodologia
    # Explanation: Foreign key referencing the methodology.
    # Nombre en es: id_metodologia
    # Explicación: Llave foránea que referencia la metodología.
    id_metodologia = Column(Integer, nullable=False)

# Name in es: ObjetivoFormulario
# Explanation: This class represents the 'objetivos_formulario' table, storing objectives for each form.
# Nombre en es: ObjetivoFormulario
# Explicación: Esta clase representa la tabla 'objetivos_formulario', almacenando objetivos para cada formulario.
class ObjetivoFormulario(Base):
    __tablename__ = "objetivos_formulario"
    # Name in es: id_objetivo
    # Explanation: Primary key of the objective, unique identifier.
    # Nombre en es: id_objetivo
    # Explicación: Clave primaria del objetivo, identificador único.
    id_objetivo = Column(Integer, primary_key=True, index=True)
    # Name in es: id_formulario
    # Explanation: Foreign key referencing the form.
    # Nombre en es: id_formulario
    # Explicación: Llave foránea que referencia el formulario.
    id_formulario = Column(Integer, nullable=False)
    # Name in es: descripcion
    # Explanation: Description of the objective.
    # Nombre en es: descripcion
    # Explicación: Descripción del objetivo.
    descripcion = Column(Text, nullable=False)
    # Name in es: tipo
    # Explanation: Type of objective, can be 'general' or 'especifico'.
    # Nombre en es: tipo
    # Explicación: Tipo de objetivo, puede ser 'general' o 'específico'.
    tipo = Column(String(20))  # 'general' o 'especifico'

# Name in es: ParticipanteFormulario
# Explanation: This class represents the 'participantes_formulario' table, storing participants for each form.
# Nombre en es: ParticipanteFormulario
# Explicación: Esta clase representa la tabla 'participantes_formulario', almacenando participantes para cada formulario.
class ParticipanteFormulario(Base):
    __tablename__ = "participantes_formulario"
    # Name in es: id_participante
    # Explanation: Primary key of the participant, unique identifier.
    # Nombre en es: id_participante
    # Explicación: Clave primaria del participante, identificador único.
    id_participante = Column(Integer, primary_key=True, index=True)
    # Name in es: id_formulario
    # Explanation: Foreign key referencing the form.
    # Nombre en es: id_formulario
    # Explicación: Llave foránea que referencia el formulario.
    id_formulario = Column(Integer, nullable=False)
    # Name in es: cargo
    # Explanation: Position or role of the participant.
    # Nombre en es: cargo
    # Explicación: Cargo o rol del participante.
    cargo = Column(String(100))
    # Name in es: nombre
    # Explanation: Name of the participant.
    # Nombre en es: nombre
    # Explicación: Nombre del participante.
    nombre = Column(String(255))
    # Name in es: firma
    # Explanation: Signature of the participant.
    # Nombre en es: firma
    # Explicación: Firma del participante.
    firma = Column(Text)

# Name in es: Metodologia
# Explanation: This class represents the 'metodologias' table, storing methodologies information.
# Nombre en es: Metodologia
# Explicación: Esta clase representa la tabla 'metodologias', almacenando información de metodologías.
class Metodologia(Base):
    __tablename__ = "metodologias"
    # Name in es: id_metodologia
    # Explanation: Primary key of the methodology, unique identifier.
    # Nombre en es: id_metodologia
    # Explicación: Clave primaria de la metodología, identificador único.
    id_metodologia = Column(Integer, primary_key=True, index=True)
    # Name in es: nombre
    # Explanation: Name of the methodology, cannot be null.
    # Nombre en es: nombre
    # Explicación: Nombre de la metodología, no puede ser nulo.
    nombre = Column(String(100), nullable=False)
    # Name in es: descripcion
    # Explanation: Description of the methodology.
    # Nombre en es: descripcion
    # Explicación: Descripción de la metodología.
    descripcion = Column(Text)
