from flask_sqlalchemy import SQLAlchemy

class DatabaseManager:
    def __init__(self):
        self.db = SQLAlchemy()

    def init_app(self, app):
        """
        Inicializa SQLAlchemy con la aplicación Flask.
        """
        self.db.init_app(app)
        with app.app_context():
            self._initialize_database()

    def close_connection(self, exception=None):
        """
        Cierra la sesión de la base de datos.
        """
        self.db.session.remove()

    def _initialize_database(self):
        """
        Crea las tablas necesarias en la base de datos.
        """
        self.db.create_all()
        print("Base de datos inicializada correctamente")

    # Exponer atributos esenciales directamente
    @property
    def Model(self):
        return self.db.Model

    @property
    def Column(self):
        return self.db.Column

    @property
    def String(self):
        return self.db.String

    @property
    def Integer(self):
        return self.db.Integer

    @property
    def DateTime(self):
        return self.db.DateTime

    @property
    def Text(self):
        return self.db.Text

    @property
    def session(self):
        """
        Exponer la sesión de SQLAlchemy.
        """
        return self.db.session

# Crear una instancia global de DatabaseManager
db_manager = DatabaseManager()
