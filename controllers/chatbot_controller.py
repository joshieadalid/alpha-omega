from flask import Blueprint, request, jsonify, Response
from result import Err
from werkzeug.datastructures import FileStorage

import services.jira_service as jir
import services.openai_service as oai
from services.jira_service import execute_jira_action
from services.openai_service import get_action_code, transcribe_audio
from services.action_t import Action

chatbot_route = Blueprint('chatbot_route', __name__)


def handle_audio(file: FileStorage, process_fn) -> tuple[Response, int]:
    """
    Maneja la transcripción de un archivo de audio y su procesamiento posterior.

    :param file: Archivo de audio enviado por el usuario.
    :param process_fn: Función para procesar el mensaje transcrito.
    :return: Respuesta JSON con el resultado o un mensaje de error.
    """
    transcription_result = transcribe_audio(file)
    if isinstance(transcription_result, Err):
        return jsonify({"error": transcription_result.unwrap_err()}), 400

    user_message = transcription_result.unwrap()
    return process_fn(user_message)


def process_text_message(user_message: str) -> str:
    """
    Procesa un mensaje de texto y ejecuta acciones en Jira.

    :param user_message: Mensaje proporcionado por el usuario.
    :return: Respuesta después de ejecutar acciones en Jira.
    """
    if not user_message:
        raise ValueError("El mensaje de texto está vacío")

    action_code = get_action_code(user_message)
    if not action_code.isdigit():
        raise ValueError("El código de acción no está en formato numérico.")

    return execute_jira_action(int(action_code), user_message)


def handle_message(user_message: str, action_fn) -> tuple[Response, int]:
    """
    Maneja un mensaje de texto y lo procesa con una función específica.

    :param user_message: Mensaje proporcionado por el usuario.
    :param action_fn: Función para ejecutar acciones basadas en el mensaje.
    :return: Respuesta JSON con el resultado o un mensaje de error.
    """
    try:
        print("Gestionando...")
        output = action_fn(user_message)
        return jsonify({"reply": output}), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500





def process_meeting_message(user_message: str) -> str:
    """
    Procesa un mensaje de reunión, extrae acciones y las ejecuta.

    :param user_message: Mensaje proporcionado por el usuario.
    :return: Respuesta después de procesar y ejecutar acciones en Jira.
    """
    actions = oai.extract_actions(user_message)
    print("Acciones extraídas: ", actions)
    return jir.process_actions(actions)


@chatbot_route.route("/chatbot/text", methods=["POST"])
def chat_text():
    user_message = request.get_json().get("message", "")
    return handle_message(user_message, process_text_message)


@chatbot_route.route("/chatbot/audio", methods=["POST"])
def chat_audio():
    if 'audio' not in request.files:
        return jsonify({"error": "No se encontró la clave 'audio' en el form-data"}), 400

    file = request.files['audio']
    return handle_audio(file, process_text_message)


@chatbot_route.route("/chatbot/meeting", methods=["POST"])
def chat_meeting():
    user_message = request.get_json().get("message", "")
    print("User message: ", user_message)
    return process_meeting_message(user_message)


@chatbot_route.route("/chatbot/meeting_audio", methods=["POST"])
def meeting_audio():
    if 'audio' not in request.files:
        return jsonify({"error": "No se encontró la clave 'audio' en el form-data"}), 400

    file = request.files['audio']
    return handle_audio(file, process_meeting_message)
