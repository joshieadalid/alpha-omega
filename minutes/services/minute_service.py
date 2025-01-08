from minutes.repositories.minute_repository import MinuteRepository
from datetime import datetime

class MinuteService:
    """
    Servicio para manejar la lógica de negocio relacionada con las minutas.
    """
    def __init__(self):
        self.repository = MinuteRepository()

    def get_all_minutes(self):
        """
        Obtiene todas las minutas.
        """
        return self.repository.get_all()

    def add_minute(self, timestamp, text):
        """
        Agrega una nueva minuta con validaciones.
        """
        if not isinstance(timestamp, datetime):
            raise TypeError("Timestamp must be an instance of datetime.datetime")
        return self.repository.add(timestamp, text)

    def get_first_minute(self):
        """
        Obtiene la primera minuta registrada.
        """
        return self.repository.get_first()

    def get_minute_by_id(self, id: int):
        return self.repository.get_by_id(id)