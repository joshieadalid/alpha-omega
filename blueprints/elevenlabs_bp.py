import os
from flask import Blueprint, request, jsonify, current_app
from services.elevenlabs_service import ElevenLabsService

# Crear el blueprint para ElevenLabs
elevenlabs_bp = Blueprint("elevenlabs", __name__)

@elevenlabs_bp.route("/stream", methods=["POST"])
def tts_stream_endpoint():
    """
    Endpoint para transmitir el audio generado a partir de texto.
    """
    data = request.json
    if not data or "text" not in data:
        return jsonify({"error": "Falta el texto en el cuerpo de la solicitud."}), 400

    text = data["text"]

    api_key = current_app.config.get("ELEVENLABS_API_KEY")
    if not api_key:
        return jsonify({"error": "API key no configurada en la aplicación."}), 500

    try:
        service = ElevenLabsService(api_key=api_key)
        audio_stream, mimetype, headers = service.tts_stream(text)
        return current_app.response_class(audio_stream, mimetype=mimetype, headers=headers)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@elevenlabs_bp.route("/mp3", methods=["POST"])
def tts_to_mp3_endpoint():
    """
    Endpoint para convertir texto a audio y guardar el resultado como MP3.
    """
    data = request.json
    if not data or "text" not in data:
        return jsonify({"error": "Falta el texto en el cuerpo de la solicitud."}), 400

    text = data["text"]

    api_key = current_app.config.get("ELEVENLABS_API_KEY")
    if not api_key:
        return jsonify({"error": "API key no configurada en la aplicación."}), 500

    try:
        service = ElevenLabsService(api_key=api_key)
        audio_stream, mimetype, headers = service.tts_to_mp3(text)
        return current_app.response_class(audio_stream, mimetype=mimetype, headers=headers)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
