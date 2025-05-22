# Name in es: Importación de create_engine
# Explanation: Imports the function to create a new SQLAlchemy engine for database connections.
# Nombre en es: Importación de create_engine
# Explicación: Importa la función para crear un nuevo motor de SQLAlchemy para conexiones a la base de datos.
from sqlalchemy import create_engine
# Name in es: Importación de sessionmaker
# Explanation: Imports the function to create new session objects for database operations.
# Nombre en es: Importación de sessionmaker
# Explicación: Importa la función para crear nuevos objetos de sesión para operaciones en la base de datos.
from sqlalchemy.orm import sessionmaker

# Name in es: DATABASE_URL
# Explanation: Connection string for the PostgreSQL database, including credentials and host information.
# Nombre en es: DATABASE_URL
# Explicación: Cadena de conexión para la base de datos PostgreSQL, incluyendo credenciales e información del host.
DATABASE_URL = "postgresql://<usuario>:<contraseña>@<host>/<db>?sslmode=require"

# Name in es: engine
# Explanation: SQLAlchemy engine instance used to manage the database connection.
# Nombre en es: engine
# Explicación: Instancia del motor de SQLAlchemy utilizada para gestionar la conexión a la base de datos.
engine = create_engine(DATABASE_URL)
# Name in es: SessionLocal
# Explanation: Factory for creating new database session objects with specific configuration.
# Nombre en es: SessionLocal
# Explicación: Fábrica para crear nuevos objetos de sesión de base de datos con configuración específica.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
