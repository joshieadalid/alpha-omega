import logging

from flask import Flask
from flask_injector import FlaskInjector

from authentication.blueprints.auth_front_bp import auth_front_bp
from chatbot.blueprints.audio_bp import audio_bp
from chatbot.blueprints.meeting_mode_bp import chatbot_bp
from chatbot.blueprints.elevenlabs_bp import elevenlabs_bp
from config import Config
from di_container import configure  # Contenedor de dependencias
from minutes.blueprints.minutes_bp import minutes_bp
from shared.extensions import db, cors, migrate


def create_app():
    app: Flask = Flask(__name__)

    # Configuración adicional
    app.config.from_object(Config)

    # Configurar logging
    logging.basicConfig(level=app.config['LOG_LEVEL'], format=app.config['LOG_FORMAT'],
        handlers=[logging.FileHandler(app.config['LOG_FILE']),  # Logs a archivo
            logging.StreamHandler()  # Logs a consola
        ])

    db.init_app(app)
    migrate.init_app(app, db)
    cors.init_app(app, resources={r"/*": {"origins": ["http://localhost:3000"]}},supports_credentials=True)

    # Registrar rutas (blueprints)
    app.register_blueprint(chatbot_bp, url_prefix='/api')
    app.register_blueprint(auth_front_bp, url_prefix='/api')
    app.register_blueprint(minutes_bp, url_prefix='/api')
    app.register_blueprint(elevenlabs_bp, url_prefix='/tts')
    app.register_blueprint(audio_bp, url_prefix='/api')

    return app


if __name__ == "__main__":
    app = create_app()
    FlaskInjector(app=app, modules=[configure])
    app.run(debug=Config.DEBUG, host=Config.HOST, port=Config.PORT)
