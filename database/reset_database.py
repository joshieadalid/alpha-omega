from app import create_app
from shared.extensions import db

def reset_database():
    app = create_app()
    with app.app_context():
        print("Eliminando tablas existentes...")
        db.drop_all()  # Elimina todas las tablas
        print("Creando tablas nuevas...")
        db.create_all()  # Crea todas las tablas nuevamente
        print("Base de datos reiniciada correctamente.")

if __name__ == "__main__":
    reset_database()
