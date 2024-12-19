from flask import Blueprint, jsonify, send_file, Response
from services.audio_service import get_audio

audio_bp = Blueprint('audio', __name__)


@audio_bp.route('/audio/<audio_id>', methods=['GET'])
def download_audio(audio_id):
    # Buscar el audio en el almacenamiento temporal
    audio_entry = get_audio(audio_id)
    if not audio_entry:
        return jsonify({"error": "Audio not found or expired"}), 404

    # Crear la respuesta con send_file
    response = Response(
        audio_entry['data'].read(),
        mimetype=audio_entry['mimetype'],
    )
    response.headers["Content-Disposition"] = audio_entry['headers'].get("Content-Disposition", "attachment; filename=audio.mp3")

    return response