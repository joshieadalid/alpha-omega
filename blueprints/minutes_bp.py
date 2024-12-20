from flask import Blueprint, jsonify, Response
from injector import inject
from weasyprint import HTML
from datetime import datetime
from services.minute_service import MinuteService, Minute
from services.openai_service import OpenAIService

minutes_bp = Blueprint('minutes_bp', __name__)


@minutes_bp.route("/minutes", methods=["GET"])
def get_minutes():
    minutes = MinuteService.get_all_minutes()
    return jsonify({"reply": [{"timestamp": minute.timestamp, "text": minute.text, "id": minute.id} for minute in minutes]})


@minutes_bp.route('/minutes/first/pdf', methods=["GET"])
@inject
def get_first_minute_pdf(openai_service: OpenAIService):
    first_minute: Minute = MinuteService.get_first_minute()
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
