import logging
from datetime import datetime
import jsonpickle
from flask import Blueprint, jsonify, Response, request, url_for
from injector import inject
from weasyprint import HTML
from werkzeug.datastructures import FileStorage

from chatbot.services.audio_service import AudioService
from chatbot.services.elevenlabs_service import ElevenLabsService
from minutes.services.minute_service import MinuteService
from chatbot.services.openai_service import OpenAIService
from chatbot.services.script_executor import ScriptExecutor

# Configurar logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s [%(levelname)s] %(message)s')
logger = logging.getLogger(__name__)

minutes_bp = Blueprint('minutes_bp', __name__)


@minutes_bp.route("/minutes", methods=["GET"])
@inject
def get_minutes(minute_service: MinuteService):
    """Obtiene todas las minutas."""
    logger.info("Solicitud recibida en /minutes")
    try:
        minutes = minute_service.get_all_minutes()
        logger.info(f"Se recuperaron {len(minutes)} minutas.")
        return jsonify({"reply": [minute.to_dict() for minute in minutes]}), 200
    except Exception as e:
        logger.exception("Error al obtener las minutas.")
        return jsonify({"error": "Ocurrió un error al obtener las minutas."}), 500


@minutes_bp.route('/minutes/first/pdf', methods=["GET"])
@inject
def get_first_minute_pdf(minute_service: MinuteService, openai_service: OpenAIService):
    """Genera un PDF de la primera minuta."""
    logger.info("Solicitud recibida en /minutes/first/pdf")
    try:
        first_minute = minute_service.get_first_minute()
        if not first_minute:
            logger.warning("No se encontraron minutas.")
            return {"error": "No minutes found"}, 404

        logger.info("Generando PDF para la primera minuta.")
        html_minute = openai_service.minute_to_html(text=first_minute.text)
        pdf_minute = HTML(string=html_minute).write_pdf()

        response = Response(pdf_minute, mimetype='application/pdf')
        response.headers['Content-Disposition'] = 'attachment; filename=first_minute.pdf'
        return response
    except Exception as e:
        logger.exception("Error al generar el PDF de la primera minuta.")
        return jsonify({"error": "Ocurrió un error al generar el PDF."}), 500


@minutes_bp.route('/minutes/<int:id>/pdf', methods=["GET"])
@inject
def get_minute_pdf(id: int, minute_service: MinuteService, openai_service: OpenAIService):
    """Genera un PDF para una minuta específica."""
    logger.info(f"Solicitud recibida en /minutes/{id}/pdf")
    try:
        minute = minute_service.get_minute_by_id(id)
        if not minute:
            logger.warning(f"No se encontró la minuta con ID: {id}")
            return {"error": "Minute not found"}, 404

        logger.info(f"Generando PDF para la minuta con ID: {id}")
        html_minute = openai_service.minute_to_html(text=minute.text)
        pdf_minute = HTML(string=html_minute).write_pdf()

        response = Response(pdf_minute, mimetype='application/pdf')
        response.headers['Content-Disposition'] = f'attachment; filename=minute_{id}.pdf'
        return response
    except Exception as e:
        logger.exception(f"Error al generar el PDF para la minuta con ID: {id}")
        return jsonify({"error": "Ocurrió un error al generar el PDF."}), 500


@minutes_bp.route("/minutes/text", methods=["POST"])
@inject
def minute_text(executor: ScriptExecutor, openai_service: OpenAIService, elevenlabs_service: ElevenLabsService,
                audio_service: AudioService, minute_service: MinuteService):
    """Crea una minuta a partir de un mensaje de texto."""
    logger.info("Solicitud recibida en /minutes/text")
    try:
        user_message = request.get_json().get("message", "")
        if not user_message:
            logger.warning("El campo 'message' está vacío.")
            return jsonify({"error": "El campo 'message' no puede estar vacío."}), 400

        logger.info(f"Mensaje recibido: {user_message}")
        execution_result = executor.execute_prompt_script(user_message)
        timestamp = datetime.now()
        minute_text = openai_service.minute_text(user_message, timestamp)
        minute = minute_service.add_minute(timestamp, minute_text)

        reply = _format_jira_response_to_text(execution_result, openai_service)
        audio_stream, mimetype, headers = elevenlabs_service.tts_to_mp3(reply)
        audio_id = audio_service.generate_audio(audio_stream, mimetype, headers)
        audio_url = url_for('audio.download_audio', audio_id=audio_id, _external=True)

        logger.info("Minuta creada y audio generado con éxito.")
        return jsonify({"reply": reply, "minute": minute.to_dict(), "audio_url": audio_url}), 200
    except Exception as e:
        logger.exception("Error al procesar la solicitud en /minutes/text")
        return jsonify({"error": "Ocurrió un error al procesar la solicitud."}), 500


@minutes_bp.route("/minutes/audio", methods=["POST"])
@inject
def minute_audio(executor: ScriptExecutor, openai_service: OpenAIService, elevenlabs_service: ElevenLabsService,
                 audio_service: AudioService, minute_service: MinuteService):
    """Crea una minuta a partir de un archivo de audio."""
    logger.info("Solicitud recibida en /minutes/audio")
    try:
        if 'audio' not in request.files:
            logger.warning("No se encontró la clave 'audio' en el form-data.")
            return jsonify({"error": "No se encontró la clave 'audio' en el form-data"}), 400

        audio_file: FileStorage = request.files['audio']
        logger.info("Archivo de audio recibido. Iniciando transcripción.")
        transcription = openai_service.transcribe_audio(audio_file)
        execution_result = executor.execute_prompt_script(transcription)
        timestamp = datetime.now()
        minute_text = openai_service.minute_text(transcription, timestamp)
        minute = minute_service.add_minute(timestamp, minute_text)

        reply = _format_jira_response_to_text(execution_result, openai_service)
        audio_stream, mimetype, headers = elevenlabs_service.tts_to_mp3(reply)
        audio_id = audio_service.generate_audio(audio_stream, mimetype, headers)
        audio_url = url_for('audio.download_audio', audio_id=audio_id, _external=True)

        logger.info("Minuta creada y audio generado correctamente.")
        return jsonify({
            "reply": reply,
            "minute": minute.to_dict(),
            "audio_url": audio_url
        }), 200
    except Exception as e:
        logger.exception("Error al procesar la solicitud en /minutes/audio")
        return jsonify({"error": "Ocurrió un error al procesar la solicitud."}), 500


def _format_jira_response_to_text(response, openai_service: OpenAIService):
    """Helper para formatear la respuesta."""
    logger.info("Formateando respuesta desde JIRA.")
    try:
        json_data = jsonpickle.encode(response, unpicklable=False)
        return openai_service.format_api_response(json_data)
    except Exception as e:
        logger.exception("Error al formatear la respuesta desde JIRA.")
        raise
