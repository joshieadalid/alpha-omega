from dotenv import load_dotenv
import os

# Cargar las variables del archivo .env
load_dotenv()

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'Prueba123')
    DEBUG = os.getenv('DEBUG', 'False').lower() in ('true', '1', 'yes')
    HOST = os.getenv('HOST', '127.0.0.1')
    PORT = int(os.getenv('PORT', 3000))
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI', 'sqlite:///example.db')

    # Configuración de OpenAI
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY', 'default-openai-api-key')

    # Configuración de Jira
    DOMAIN = os.getenv('DOMAIN', 'default-domain')
    ATLASSIAN_USERNAME = os.getenv('ATLASSIAN_USERNAME', 'default-username')
    ATLASSIAN_API_KEY = os.getenv('ATLASSIAN_API_KEY', 'default-api-key')

    # Elevenlabs
    ELEVENLABS_API_KEY = os.getenv('ELEVENLABS_API_KEY')
    UPLOAD_FOLDER = "uploads"