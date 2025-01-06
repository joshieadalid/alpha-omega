from datetime import datetime

from services.database_manager import db_manager

class Minute(db_manager.Model):
    """
    Modelo para representar la tabla 'minutes' en la base de datos.
    """
    __tablename__ = 'minutes'

    id = db_manager.Column(db_manager.Integer, primary_key=True)
    timestamp = db_manager.Column(db_manager.DateTime, nullable=False)
    text = db_manager.Column(db_manager.Text, nullable=False)

    @classmethod
    def get_all(cls):
        """
        Obtiene todas las minutas de la base de datos.
        """
        try:
            return cls.query.all()
        except Exception as e:
            print(f"Error al obtener las minutas: {e}")
            return []

    @classmethod
    def add(cls, timestamp, text):
        """
        Agrega una nueva minuta a la base de datos.
        """
        try:
            # Validar que timestamp sea un objeto datetime
            if not isinstance(timestamp, datetime):
                raise TypeError("Timestamp must be an instance of datetime.datetime")

            # Crear una nueva minuta y guardarla en la base de datos
            new_minute = cls(timestamp=timestamp, text=text)
            db_manager.session.add(new_minute)
            db_manager.session.commit()
            return new_minute
        except Exception as e:
            db_manager.session.rollback()
            print(f"Error al agregar la minuta: {e}")
            return None

    @classmethod
    def get_first(cls):
        """
        Obtiene la primera minuta registrada en la base de datos.
        """
        try:
            return cls.query.first()
        except Exception as e:
            print(f"Error al obtener la primera minuta: {e}")
            return None

    def to_dict(self):
        return {
            "id": self.id,
            "timestamp": self.timestamp.isoformat(),  # Convertir a formato ISO 8601
            "text": self.text,
        }
