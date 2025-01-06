import os

from dotenv import load_dotenv

# Cargar las variables del archivo .env
load_dotenv()


class Config:
    SECRET_KEY: str = os.getenv('SECRET_KEY', 'Prueba123')
    DEBUG: bool = os.getenv('DEBUG', 'False').lower() in ('true', '1', 'yes')
    HOST: str = os.getenv('HOST', '127.0.0.1')
    PORT: int = int(os.getenv('PORT', 8080))
    SQLALCHEMY_DATABASE_URI: str = os.getenv('SQLALCHEMY_DATABASE_URI', 'sqlite:///example.db')

    # Configuración de OpenAI
    OPENAI_API_KEY: str = os.getenv('OPENAI_API_KEY', 'default-openai-api-key')

    # Configuración de Jira
    DOMAIN: str = os.getenv('DOMAIN', 'default-domain')
    ATLASSIAN_USERNAME: str = os.getenv('ATLASSIAN_USERNAME', 'default-username')
    ATLASSIAN_API_KEY: str = os.getenv('ATLASSIAN_API_KEY', 'default-api-key')

    # Elevenlabs
    ELEVENLABS_API_KEY: str = os.getenv('ELEVENLABS_API_KEY')
    UPLOAD_FOLDER: str = "uploads"
