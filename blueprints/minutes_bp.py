from datetime import datetime

import jsonpickle
from flask import Blueprint, jsonify, Response, request, url_for
from injector import inject
from weasyprint import HTML
from werkzeug.datastructures import FileStorage

from models.minute import Minute
from services.audio_service import AudioService
from services.elevenlabs_service import ElevenLabsService
from services.openai_service import OpenAIService
from services.script_executor import ScriptExecutor

minutes_bp = Blueprint('minutes_bp', __name__)


@minutes_bp.route("/minutes", methods=["GET"])
def get_minutes():
    minutes = Minute.get_all()
    print(f'{minutes=}')
    return jsonify({"reply": [minute.to_dict() for minute in minutes]})


@minutes_bp.route('/minutes/first/pdf', methods=["GET"])
@inject
def get_first_minute_pdf(openai_service: OpenAIService):
    first_minute: Minute = Minute.get_first()
    html_minute: str = openai_service.minute_to_html(text=first_minute.text)
    pdf_minute = HTML(string=html_minute).write_pdf()

    # Crear la respuesta HTTP con el PDF
    response = Response(pdf_minute, mimetype='application/pdf')
    response.headers['Content-Disposition'] = 'attachment; filename=first_minute.pdf'
    return response


@minutes_bp.route('/minutes/<int:id>/pdf', methods=["GET"])
@inject
def get_minute_pdf(id: int, openai_service: OpenAIService):
    # Obtener la minuta específica por ID
    minute: Minute = Minute.query.get(id)
    if not minute:
        return {"error": "Minute not found"}, 404

    # Convertir el texto de la minuta a HTML
    html_minute: str = openai_service.minute_to_html(text=minute.text)

    # Generar el PDF desde el HTML
    pdf_minute = HTML(string=html_minute).write_pdf()

    # Crear la respuesta HTTP con el PDF
    response = Response(pdf_minute, mimetype='application/pdf')
    response.headers['Content-Disposition'] = f'attachment; filename=minute_{id}.pdf'
    return response


@minutes_bp.route("/minutes/text", methods=["POST"])
@inject
def minute(executor: ScriptExecutor, openai_service: OpenAIService, elevenlabs_service: ElevenLabsService,
           audio_service: AudioService):
    user_message = request.get_json().get("message", "")
    print("User message:", user_message)
    execution_result: str = executor.execute_prompt_script(user_message)
    timestamp = datetime.now()
    minute_text: str = openai_service.minute_text(user_message, timestamp)
    minute: Minute = Minute.add(timestamp, minute_text)  # Resultado almacenado

    reply: str = _format_jira_response_to_text(execution_result, openai_service)
    audio_stream, mimetype, headers = elevenlabs_service.tts_to_mp3(reply)
    audio_id: str = audio_service.generate_audio(audio_stream, mimetype, headers)
    audio_url = url_for('audio.download_audio', audio_id=audio_id, _external=True)

    return jsonify({"reply": reply, "minute": minute.to_dict(), "audio_url": audio_url}), 200


@minutes_bp.route("/minutes/audio", methods=["POST"])
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
    minute: Minute = Minute.add(timestamp, minute_text)  # Resultado almacenado

    reply: str = _format_jira_response_to_text(response, openai_service)
    audio_stream, mimetype, headers = elevenlabs_service.tts_to_mp3(reply)
    audio_id: str = audio_service.generate_audio(audio_stream, mimetype, headers)
    audio_url = url_for('audio.download_audio', audio_id=audio_id, _external=True)

    return jsonify({
        "reply": reply,
        "minute": minute.to_dict(),
        "audio_url": audio_url
    }), 200


# Helper para formatear la respuesta
def _format_jira_response_to_text(response, openai_service: OpenAIService):
    json_data = jsonpickle.encode(response, unpicklable=False)
    return openai_service.format_api_response(json_data)
