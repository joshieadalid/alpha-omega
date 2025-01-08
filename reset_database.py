import logging
from app import create_app
from shared.extensions import db

# Configurar logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s [%(levelname)s] %(message)s')
logger = logging.getLogger(__name__)

def reset_database():
    app = create_app()
    with app.app_context():
        logger.info("Eliminando tablas existentes...")
        db.drop_all()  # Elimina todas las tablas
        logger.info("Creando tablas nuevas...")
        db.create_all()  # Crea todas las tablas nuevamente
        logger.info("Base de datos reiniciada correctamente.")

if __name__ == "__main__":
    reset_database()
