from flask import Blueprint, request, jsonify
from werkzeug.datastructures import FileStorage
from jira import JIRA
from services.openai_service import OpenAIService
from services.script_executor import ScriptExecutor
from config import Config  # Configuración global
import openai
import jsonpickle

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
    model_type="gpt-4o-mini",
)

executor = ScriptExecutor(
    openai_service=openai_service,
    jira_client=jira_client
)


# Helper para formatear la respuesta
def format_response(response):
    json_data = jsonpickle.encode(response, unpicklable=False)
    return openai_service.format_api_response(json_data)


@chatbot_bp.route("/meeting", methods=["POST"])
def chat_meeting():
    """Endpoint para manejar mensajes de texto."""
    user_message = request.get_json().get("message", "")
    print("User message:", user_message)
    response = executor.execute_prompt_script(user_message)
    formatted_response = format_response(response)
    return jsonify({"reply": formatted_response}), 200


@chatbot_bp.route("/meeting_audio", methods=["POST"])
def meeting_audio():
    """Endpoint para manejar archivos de audio."""
    if 'audio' not in request.files:
        return jsonify({"error": "No se encontró la clave 'audio' en el form-data"}), 400

    audio_file: FileStorage = request.files['audio']
    transcription = openai_service.transcribe_audio(audio_file)
    response = executor.execute_prompt_script(transcription)
    formatted_response = format_response(response)
    return jsonify({"reply": formatted_response}), 200


@chatbot_bp.route("/commands_mode", methods=["POST"])
def commands_mode():
    """Endpoint para comandos directos."""
    user_message = request.get_json().get("message", "")
    print("User message:", user_message)
    response = executor.execute_prompt_script(user_message)
    formatted_response = format_response(response)
    return jsonify({"reply": formatted_response}), 200
