from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def init_db(app):
    db.init_app(app)
    with app.app_context():
        from services.minute_service import Minute  # Importa el modelo
        db.create_all()

def close_database_connection(exception=None):
    db.session.remove()
