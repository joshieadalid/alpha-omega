from flask import Blueprint, request, jsonify
from werkzeug.datastructures import FileStorage
from jira import JIRA
from services.openai_service import OpenAIService
from services.script_executor import ScriptExecutor
from config import Config  # Configuración global
import openai
import jsonpickle
from utils.auth import jwt_required

# Crear Blueprint con prefijo '/chatbot'
chatbot_bp = Blueprint('chatbot_route', __name__)

# Configuración de OpenAI
openai.api_key = Config.OPENAI_API_KEY
openai_client = openai

# Configuración de Jira
jira_client = JIRA(
    server=f"https://{Config.DOMAIN}.atlassian.net",
    basic_auth=(Config.ATLASSIAN_USERNAME, Config.ATLASSIAN_API_KEY)
)

# Inicialización de servicios
openai_service = OpenAIService(
    openai_client=openai_client,
    model_type="gpt-4o",
)

executor = ScriptExecutor(
    openai_service=openai_service,
    jira_client=jira_client
)


# Helper para formatear la respuesta
def _format_response(response):
    json_data = jsonpickle.encode(response, unpicklable=False)
    print(json_data)
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

from datetime import datetime
@chatbot_bp.route("/minutes_text", methods=["POST"])
def minute():
    user_message = request.get_json().get("message", "")
    print("User message:", user_message)
    response:str = executor.execute_prompt_script(user_message)
    minute: str = openai_service.generate_minute(user_message, datetime.now().strftime("%d de %B de %Y, %H:%M:%S"))
    formatted_response:str = _format_response(response)
    return jsonify({"reply": formatted_response, "minute": minute}), 200

# /api/minutes
# Ruta para obtener todas las minutas
@chatbot_bp.route("/api/minutes", methods=["GET"])
def get_minutes():
    minutes = MinuteService.get_all_minutes()
    return jsonify({
        "reply": [
            {"timestamp": minute.timestamp, "text": minute.text} for minute in minutes
        ]
    })


# Ruta para agregar una nueva minuta (ejemplo)
@chatbot_bp.route("/api/minutes", methods=["POST"])
def add_minute():
    # Simula datos para agregar
    timestamp = "2024-12-18T12:00:00"
    text = "Nueva minuta de prueba"
    new_minute = MinuteService.add_minute(timestamp, text)
    return jsonify({
        "message": "Minuta agregada exitosamente",
        "minute": {"timestamp": new_minute.timestamp, "text": new_minute.text}
    })
