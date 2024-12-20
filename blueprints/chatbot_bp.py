from datetime import datetime

import jsonpickle
from flask import Blueprint, request, jsonify, url_for
from injector import inject
from werkzeug.datastructures import FileStorage

from services.audio_service import AudioService
from services.elevenlabs_service import ElevenLabsService
from services.minute_service import MinuteService, Minute
from services.openai_service import OpenAIService
from services.script_executor import ScriptExecutor

# Crear Blueprint con prefijo '/chatbot'
chatbot_bp = Blueprint('chatbot_route', __name__)


# Helper para formatear la respuesta
def _format_jira_response_to_text(response, openai_service: OpenAIService):
    json_data = jsonpickle.encode(response, unpicklable=False)
    return openai_service.format_api_response(json_data)


@chatbot_bp.route("/meeting", methods=["POST"])
@inject
def chat_meeting(executor: ScriptExecutor, openai_service: OpenAIService):
    """Endpoint para manejar mensajes de texto."""
    user_message = request.get_json().get("message", "")
    print("User message:", user_message)
    response = executor.execute_prompt_script(user_message)
    formatted_response = _format_jira_response_to_text(response, openai_service)
    return jsonify({"reply": formatted_response}), 200


@chatbot_bp.route("/meeting_audio", methods=["POST"])
@inject
def meeting_audio(executor: ScriptExecutor, openai_service: OpenAIService):
    """Endpoint para manejar archivos de audio."""
    if 'audio' not in request.files:
        return jsonify({"error": "No se encontró la clave 'audio' en el form-data"}), 400

    audio_file: FileStorage = request.files['audio']
    transcription = openai_service.transcribe_audio(audio_file)
    response = executor.execute_prompt_script(transcription)
    formatted_response = _format_jira_response_to_text(response, openai_service)
    return jsonify({"reply": formatted_response}), 200


@chatbot_bp.route("/minutes/text", methods=["POST"])
@inject
def minute(executor: ScriptExecutor, openai_service: OpenAIService, elevenlabs_service: ElevenLabsService,
           audio_service: AudioService):
    user_message = request.get_json().get("message", "")
    print("User message:", user_message)
    execution_result: str = executor.execute_prompt_script(user_message)
    timestamp = datetime.now().strftime("%d de %B de %Y, %H:%M:%S")
    minute_text: str = openai_service.minute_text(user_message, timestamp)
    minute: Minute = MinuteService.add_minute(timestamp, minute_text)  # Resultado almacenado

    reply: str = _format_jira_response_to_text(execution_result, openai_service)
    audio_stream, mimetype, headers = elevenlabs_service.tts_to_mp3(reply)
    audio_id: str = audio_service.generate_audio(audio_stream, mimetype, headers)
    audio_url = url_for('audio.download_audio', audio_id=audio_id, _external=True)

    return jsonify({"reply": reply, "minute": minute.to_dict(), "audio_url": audio_url}), 200


@chatbot_bp.route("/minutes/audio", methods=["POST"])
@inject
def minute_audio(executor: ScriptExecutor, openai_service: OpenAIService, elevenlabs_service: ElevenLabsService,
                  audio_service: AudioService):
    """Endpoint para manejar archivos de audio y generar minuta."""
    if 'audio' not in request.files:
        return jsonify({"error": "No se encontró la clave 'audio' en el form-data"}), 400

    audio_file: FileStorage = request.files['audio']
    transcription = openai_service.transcribe_audio(audio_file)
    response = executor.execute_prompt_script(transcription)
    timestamp = datetime.now().strftime("%d de %B de %Y, %H:%M:%S")
    minute_text: str = openai_service.minute_text(transcription, timestamp)
    minute: Minute = MinuteService.add_minute(timestamp, minute_text)  # Resultado almacenado

    reply: str = _format_jira_response_to_text(response, openai_service)
    audio_stream, mimetype, headers = elevenlabs_service.tts_to_mp3(reply)
    audio_id: str = audio_service.generate_audio(audio_stream, mimetype, headers)
    audio_url = url_for('audio.download_audio', audio_id=audio_id, _external=True)

    return jsonify({
        "reply": reply,
        "minute": minute.to_dict(),
        "audio_url": audio_url
    }), 200
