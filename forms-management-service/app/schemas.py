from pydantic import BaseModel
from datetime import date

# Name in es: FormularioBase
# Explanation: Base schema for form data, used as a parent for other form schemas.
# Nombre en es: FormularioBase
# Explicación: Esquema base para datos de formulario, usado como padre para otros esquemas de formulario.
class FormularioBase(BaseModel):
    # Name in es: id_empresa
    # Explanation: Company ID related to the form.
    # Nombre en es: id_empresa
    # Explicación: ID de la empresa relacionada con el formulario.
    id_empresa: int
    # Name in es: fecha
    # Explanation: Date when the form was filled.
    # Nombre en es: fecha
    # Explicación: Fecha en que se llenó el formulario.
    fecha: date
    # Name in es: ciudad
    # Explanation: City where the form was filled, optional.
    # Nombre en es: ciudad
    # Explicación: Ciudad donde se llenó el formulario, opcional.
    ciudad: str | None = None
    # Name in es: nombre_software
    # Explanation: Name of the software evaluated, optional.
    # Nombre en es: nombre_software
    # Explicación: Nombre del software evaluado, opcional.
    nombre_software: str | None = None
    # Name in es: id_usuario
    # Explanation: User ID related to the form.
    # Nombre en es: id_usuario
    # Explicación: ID del usuario relacionado con el formulario.
    id_usuario: int
    # Name in es: id_metodologia
    # Explanation: Methodology ID related to the form.
    # Nombre en es: id_metodologia
    # Explicación: ID de la metodología relacionada con el formulario.
    id_metodologia: int

# Name in es: FormularioCreate
# Explanation: Schema for creating a new form, inherits from FormularioBase.
# Nombre en es: FormularioCreate
# Explicación: Esquema para crear un nuevo formulario, hereda de FormularioBase.
class FormularioCreate(FormularioBase):
    pass

# Name in es: Formulario
# Explanation: Schema representing a form with its ID, used for responses.
# Nombre en es: Formulario
# Explicación: Esquema que representa un formulario con su ID, usado para respuestas.
class Formulario(FormularioBase):
    # Name in es: id_formulario
    # Explanation: Unique identifier of the form.
    # Nombre en es: id_formulario
    # Explicación: Identificador único del formulario.
    id_formulario: int
    # Name in es: Config
    # Explanation: Enables ORM mode for compatibility with ORM objects.
    # Nombre en es: Config
    # Explicación: Habilita el modo ORM para compatibilidad con objetos ORM.
    class Config:
        orm_mode = True

# Name in es: ObjetivoFormularioBase
# Explanation: Base schema for objective data, used as a parent for other objective schemas.
# Nombre en es: ObjetivoFormularioBase
# Explicación: Esquema base para datos de objetivo, usado como padre para otros esquemas de objetivo.
class ObjetivoFormularioBase(BaseModel):
    # Name in es: id_formulario
    # Explanation: Form ID related to the objective.
    # Nombre en es: id_formulario
    # Explicación: ID del formulario relacionado con el objetivo.
    id_formulario: int
    # Name in es: descripcion
    # Explanation: Description of the objective.
    # Nombre en es: descripcion
    # Explicación: Descripción del objetivo.
    descripcion: str
    # Name in es: tipo
    # Explanation: Type of objective, can be 'general' or 'especifico'.
    # Nombre en es: tipo
    # Explicación: Tipo de objetivo, puede ser 'general' o 'específico'.
    tipo: str

# Name in es: ObjetivoFormularioCreate
# Explanation: Schema for creating a new objective, inherits from ObjetivoFormularioBase.
# Nombre en es: ObjetivoFormularioCreate
# Explicación: Esquema para crear un nuevo objetivo, hereda de ObjetivoFormularioBase.
class ObjetivoFormularioCreate(ObjetivoFormularioBase):
    pass

# Name in es: ObjetivoFormulario
# Explanation: Schema representing an objective with its ID, used for responses.
# Nombre en es: ObjetivoFormulario
# Explicación: Esquema que representa un objetivo con su ID, usado para respuestas.
class ObjetivoFormulario(ObjetivoFormularioBase):
    # Name in es: id_objetivo
    # Explanation: Unique identifier of the objective.
    # Nombre en es: id_objetivo
    # Explicación: Identificador único del objetivo.
    id_objetivo: int
    # Name in es: Config
    # Explanation: Enables ORM mode for compatibility with ORM objects.
    # Nombre en es: Config
    # Explicación: Habilita el modo ORM para compatibilidad con objetos ORM.
    class Config:
        orm_mode = True

# Name in es: ParticipanteFormularioBase
# Explanation: Base schema for participant data, used as a parent for other participant schemas.
# Nombre en es: ParticipanteFormularioBase
# Explicación: Esquema base para datos de participante, usado como padre para otros esquemas de participante.
class ParticipanteFormularioBase(BaseModel):
    # Name in es: id_formulario
    # Explanation: Form ID related to the participant.
    # Nombre en es: id_formulario
    # Explicación: ID del formulario relacionado con el participante.
    id_formulario: int
    # Name in es: cargo
    # Explanation: Position or role of the participant, optional.
    # Nombre en es: cargo
    # Explicación: Cargo o rol del participante, opcional.
    cargo: str | None = None
    # Name in es: nombre
    # Explanation: Name of the participant, optional.
    # Nombre en es: nombre
    # Explicación: Nombre del participante, opcional.
    nombre: str | None = None
    # Name in es: firma
    # Explanation: Signature of the participant, optional.
    # Nombre en es: firma
    # Explicación: Firma del participante, opcional.
    firma: str | None = None

# Name in es: ParticipanteFormularioCreate
# Explanation: Schema for creating a new participant, inherits from ParticipanteFormularioBase.
# Nombre en es: ParticipanteFormularioCreate
# Explicación: Esquema para crear un nuevo participante, hereda de ParticipanteFormularioBase.
class ParticipanteFormularioCreate(ParticipanteFormularioBase):
    pass

# Name in es: ParticipanteFormulario
# Explanation: Schema representing a participant with its ID, used for responses.
# Nombre en es: ParticipanteFormulario
# Explicación: Esquema que representa un participante con su ID, usado para respuestas.
class ParticipanteFormulario(ParticipanteFormularioBase):
    # Name in es: id_participante
    # Explanation: Unique identifier of the participant.
    # Nombre en es: id_participante
    # Explicación: Identificador único del participante.
    id_participante: int
    # Name in es: Config
    # Explanation: Enables ORM mode for compatibility with ORM objects.
    # Nombre en es: Config
    # Explicación: Habilita el modo ORM para compatibilidad con objetos ORM.
    class Config:
        orm_mode = True

# Name in es: MetodologiaBase
# Explanation: Base schema for methodology data, used as a parent for other methodology schemas.
# Nombre en es: MetodologiaBase
# Explicación: Esquema base para datos de metodología, usado como padre para otros esquemas de metodología.
class MetodologiaBase(BaseModel):
    # Name in es: nombre
    # Explanation: Name of the methodology.
    # Nombre en es: nombre
    # Explicación: Nombre de la metodología.
    nombre: str
    # Name in es: descripcion
    # Explanation: Description of the methodology, optional.
    # Nombre en es: descripcion
    # Explicación: Descripción de la metodología, opcional.
    descripcion: str | None = None

# Name in es: MetodologiaCreate
# Explanation: Schema for creating a new methodology, inherits from MetodologiaBase.
# Nombre en es: MetodologiaCreate
# Explicación: Esquema para crear una nueva metodología, hereda de MetodologiaBase.
class MetodologiaCreate(MetodologiaBase):
    pass

# Name in es: Metodologia
# Explanation: Schema representing a methodology with its ID, used for responses.
# Nombre en es: Metodologia
# Explicación: Esquema que representa una metodología con su ID, usado para respuestas.
class Metodologia(MetodologiaBase):
    # Name in es: id_metodologia
    # Explanation: Unique identifier of the methodology.
    # Nombre en es: id_metodologia
    # Explicación: Identificador único de la metodología.
    id_metodologia: int
    # Name in es: Config
    # Explanation: Enables ORM mode for compatibility with ORM objects.
    # Nombre en es: Config
    # Explicación: Habilita el modo ORM para compatibilidad con objetos ORM.
    class Config:
        orm_mode = True
