from minutes.models.minute import Minute
from shared.extensions import db

class MinuteRepository:
    """
    Repositorio para manejar operaciones de la base de datos relacionadas con 'Minute'.
    """
    @staticmethod
    def get_all():
        """
        Obtiene todas las minutas de la base de datos.
        """
        try:
            return Minute.query.all()
        except Exception as e:
            print(f"Error al obtener las minutas: {e}")
            return []

    @staticmethod
    def add(timestamp, text):
        """
        Agrega una nueva minuta a la base de datos.
        """
        try:
            new_minute = Minute(timestamp=timestamp, text=text)
            db.session.add(new_minute)
            db.session.commit()
            return new_minute
        except Exception as e:
            db.session.rollback()
            print(f"Error al agregar la minuta: {e}")
            return None

    @staticmethod
    def get_first():
        """
        Obtiene la primera minuta registrada en la base de datos.
        """
        try:
            return Minute.query.order_by(Minute.timestamp.asc()).first()
        except Exception as e:
            print(f"Error al obtener la primera minuta: {e}")
            return None

    @staticmethod
    def get_by_id(id: int):
        return Minute.query.get(id)