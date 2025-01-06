import jsonpickle
from flask import Blueprint, request, jsonify
from injector import inject
from werkzeug.datastructures import FileStorage

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
