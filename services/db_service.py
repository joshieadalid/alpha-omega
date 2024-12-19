from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def init_db(app):
    db.init_app(app)
    with app.app_context():
        from services.minute_service import Minute
        db.create_all()
        print("Base de datos inicializada correctamente")


def close_database_connection(exception=None):
    db.session.remove()
