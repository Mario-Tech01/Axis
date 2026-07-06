from typing import Generator
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base, Session
from axis.infraestructure.config import settings

# 1. Creamos el motor utilizando la URL inyectada desde las variables de entorno (.env)
engine = create_engine(
    settings.DATABASE_URL,
    # pool_pre_ping ayuda a reconectar automáticamente si la conexión con Postgres se cae
    pool_pre_ping=True 
)

# 2. Creamos la fábrica de sesiones (SessionLocal)
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# 3. La Base declarativa para los Modelos ORM de SQLAlchemy 
# OJO: Estos son modelos de base de datos (infraestructura), NO tus entidades de dominio.
Base = declarative_base()

# 4. Una función generadora para manejar el ciclo de vida de la sesión (Dependency Injection)
def get_db() -> Generator[Session, None, None]:
    """
    Provee una sesión de base de datos por cada petición web
    y la cierra automáticamente al terminar.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()