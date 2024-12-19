from datetime import datetime

import jsonpickle
import openai
from flask import Blueprint, request, jsonify, url_for
from jira import JIRA
from werkzeug.datastructures import FileStorage
from flask import Blueprint, request, jsonify, current_app
from blueprints.elevenlabs_bp import tts_stream_endpoint
from config import Config  # Configuración global
from services.minute_service import MinuteService
from services.openai_service import OpenAIService
from services.script_executor import ScriptExecutor
from services.elevenlabs_service import ElevenLabsService
from services.audio_service import generate_audio
# Crear Blueprint con prefijo '/chatbot'
chatbot_bp = Blueprint('chatbot_route', __name__)

# Configuración de OpenAI
openai.api_key = Config.OPENAI_API_KEY
openai_client = openai

# Configuración de Jira
jira_client = JIRA(server=f"https://{Config.DOMAIN}.atlassian.net",
    basic_auth=(Config.ATLASSIAN_USERNAME, Config.ATLASSIAN_API_KEY))

# Inicialización de servicios
openai_service = OpenAIService(openai_client=openai_client, model_type="gpt-4o-mini", )

executor = ScriptExecutor(openai_service=openai_service, jira_client=jira_client)
elevenlabs_service = ElevenLabsService(Config.ELEVENLABS_API_KEY)

# Helper para formatear la respuesta
def _format_response(response):
    json_data = jsonpickle.encode(response, unpicklable=False)
    return openai_service.format_api_response(json_data)


@chatbot_bp.route("/meeting", methods=["POST"])
def chat_meeting():
    """Endpoint para manejar mensajes de texto."""
    user_message = request.get_json().get("message", "")
    print("User message:", user_message)
    response = executor.execute_prompt_script(user_message)
    formatted_response = _format_response(response)
    return jsonify({"reply": formatted_response}), 200


@chatbot_bp.route("/meeting_audio", methods=["POST"])
def meeting_audio():
    """Endpoint para manejar archivos de audio."""
    if 'audio' not in request.files:
        return jsonify({"error": "No se encontró la clave 'audio' en el form-data"}), 400

    audio_file: FileStorage = request.files['audio']
    transcription = openai_service.transcribe_audio(audio_file)
    response = executor.execute_prompt_script(transcription)
    formatted_response = _format_response(response)
    return jsonify({"reply": formatted_response}), 200


@chatbot_bp.route("/minutes_text", methods=["POST"])
def minute():
    user_message = request.get_json().get("message", "")
    print("User message:", user_message)
    execution_result: str = executor.execute_prompt_script(user_message)
    minute: str = openai_service.generate_minute(user_message, datetime.now().strftime("%d de %B de %Y, %H:%M:%S"))
    timestamp = datetime.now().strftime("%d de %B de %Y, %H:%M:%S")
    MinuteService.add_minute(timestamp, minute)
    formatted_response: str = _format_response(execution_result)
    audio_stream, mimetype, headers = elevenlabs_service.tts_to_mp3(formatted_response)
    audio_id = generate_audio(audio_stream,mimetype, headers)
    audio_url = url_for('audio.download_audio', audio_id=audio_id, _external=True)
    return jsonify({
        "reply": formatted_response,
        "minute": minute,
        "audio_url": audio_url
    }), 200
