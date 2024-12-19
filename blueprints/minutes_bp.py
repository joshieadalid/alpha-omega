from flask import Blueprint, jsonify
from services.minute_service import MinuteService

minutes_bp = Blueprint('minutes_bp', __name__)

@minutes_bp.route("/minutes", methods=["GET"])
def get_minutes():
    minutes = MinuteService.get_all_minutes()
    return jsonify({
        "reply": [
            {"timestamp": minute.timestamp, "text": minute.text} for minute in minutes
        ]
    })

@minutes_bp.route("/minutes", methods=["POST"])
def add_minute():
    # Datos simulados; sustituye por datos del cliente
    timestamp = "2024-12-18T13:00:00"
    text = "Minuta de ejemplo"
    new_minute = MinuteService.add_minute(timestamp, text)
    return jsonify({
        "message": "Minuta agregada exitosamente",
        "minute": {"timestamp": new_minute.timestamp, "text": new_minute.text}
    })
