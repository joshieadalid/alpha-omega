import uuid
import time
from typing import IO, Dict, Optional

class AudioService:
    def __init__(self, expiration_time: int = 60):
        """
        Inicializa el servicio de audio con un almacenamiento temporal y tiempo de expiración.

        :param expiration_time: Tiempo de expiración de los audios en segundos.
        """
        self.audio_store = {}
        self.expiration_time = expiration_time

    def generate_audio(self, audio_stream: IO[bytes], mimetype: str, headers: Dict[str, str]) -> str:
        """
        Almacena un flujo de audio proporcionado externamente y devuelve un identificador único.

        :param audio_stream: El flujo de audio (archivo en memoria o BytesIO).
        :param mimetype: El tipo MIME del audio (por ejemplo, 'audio/mpeg').
        :param headers: Los headers adicionales necesarios (por ejemplo, Content-Disposition).
        :return: Identificador único del audio.
        """
        # Generar identificador único
        audio_id = str(uuid.uuid4())
        self.audio_store[audio_id] = {
            'data': audio_stream,
            'timestamp': time.time(),
            'mimetype': mimetype,
            'headers': headers
        }
        return audio_id

    def get_audio(self, audio_id: str) -> Optional[Dict]:
        """
        Recupera un audio almacenado temporalmente por su identificador único.

        :param audio_id: Identificador del audio.
        :return: Datos del audio o None si no existe o ha expirado.
        """
        audio_entry = self.audio_store.get(audio_id)
        if not audio_entry:
            return None

        # Verificar expiración
        if time.time() - audio_entry['timestamp'] > self.expiration_time:
            del self.audio_store[audio_id]  # Eliminar audio expirado
            return None

        return audio_entry
