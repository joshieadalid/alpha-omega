from flask import Blueprint, request, jsonify, current_app
from injector import inject
from services.elevenlabs_service import ElevenLabsService

# Crear el blueprint para ElevenLabs
elevenlabs_bp = Blueprint("elevenlabs", __name__)

@elevenlabs_bp.route("/stream", methods=["POST"])
@inject
def tts_stream_endpoint(service: ElevenLabsService):
    """
    Endpoint para transmitir el audio generado a partir de texto.
    """
    data = request.json
    if not data or "text" not in data:
        return jsonify({"error": "Falta el texto en el cuerpo de la solicitud."}), 400

    text = data["text"]

    try:
        audio_stream, mimetype, headers = service.tts_stream(text)
        return current_app.response_class(audio_stream, mimetype=mimetype, headers=headers)
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@elevenlabs_bp.route("/mp3", methods=["POST"])
@inject
def tts_to_mp3_endpoint(service: ElevenLabsService):
    """
    Endpoint para convertir texto a audio y guardar el resultado como MP3.
    """
    data = request.json
    if not data or "text" not in data:
        return jsonify({"error": "Falta el texto en el cuerpo de la solicitud."}), 400

    text = data["text"]

    try:
        audio_stream, mimetype, headers = service.tts_to_mp3(text)
        return current_app.response_class(audio_stream, mimetype=mimetype, headers=headers)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
