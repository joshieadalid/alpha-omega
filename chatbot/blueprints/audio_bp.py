from flask import Blueprint, jsonify, Response
from injector import inject
from chatbot.services.audio_service import AudioService

audio_bp = Blueprint('audio', __name__)

@audio_bp.route('/audio/<audio_id>', methods=['GET'])
@inject
def download_audio(audio_id, audio_service: AudioService):
    """
    Endpoint para descargar un archivo de audio almacenado temporalmente.
    """
    # Buscar el audio utilizando el servicio inyectado
    audio_entry = audio_service.get_audio(audio_id)
    if not audio_entry:
        return jsonify({"error": "Audio not found or expired"}), 404

    # Crear la respuesta con el archivo de audio
    response = Response(
        audio_entry['data'].read(),
        mimetype=audio_entry['mimetype'],
    )
    response.headers["Content-Disposition"] = audio_entry['headers'].get("Content-Disposition", "attachment; filename=audio.mp3")

    return response
