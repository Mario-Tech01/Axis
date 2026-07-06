from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    # Define tus variables y sus tipos de datos
    DEBUG: bool = False
    PROJECT_NAME: str
    DATABASE_URL: str

    # Esta línea es el truco: le dice a Pydantic que lea el archivo .env
    model_config = SettingsConfigDict(env_file=".env")

# Instanciamos la configuración para usarla en el proyecto
settings = Settings()