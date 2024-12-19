import uuid
import time
from typing import IO, Dict

# Almacenamiento temporal
audio_store = {}
AUDIO_EXPIRATION_TIME = 60  # En segundos


def generate_audio(audio_stream: IO[bytes], mimetype: str, headers: Dict[str, str]) -> str:
    """
    Almacena un flujo de audio proporcionado externamente y devuelve un identificador único.

    :param audio_stream: El flujo de audio (archivo en memoria o BytesIO).
    :param mimetype: El tipo MIME del audio (por ejemplo, 'audio/mpeg').
    :param headers: Los headers adicionales necesarios (por ejemplo, Content-Disposition).
    :return: Identificador único del audio.
    """
    # Generar identificador único
    audio_id = str(uuid.uuid4())
    audio_store[audio_id] = {
        'data': audio_stream,
        'timestamp': time.time(),
        'mimetype': mimetype,
        'headers': headers
    }
    return audio_id


def get_audio(audio_id: str):
    """
    Recupera un audio almacenado temporalmente por su identificador único.

    :param audio_id: Identificador del audio.
    :return: Datos del audio o None si no existe.
    """
    return audio_store.get(audio_id)
