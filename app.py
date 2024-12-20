from flask import Flask
from flask_injector import FlaskInjector

from blueprints.audio_bp import audio_bp
from blueprints.auth_bp import auth_bp
from blueprints.chatbot_bp import chatbot_bp
from blueprints.elevenlabs_bp import elevenlabs_bp
from blueprints.frontend_bp import frontend_bp
from blueprints.minutes_bp import minutes_bp
from blueprints.modes_bp import modes_bp
# Blueprints
from blueprints.root import root_bp
from config import Config
# Contenedor de dependencias
from di_container import configure
# Servicios
from services.db_service import init_db, close_database_connection


def create_app():
    app = Flask(__name__, static_folder=None)

    # Configuración adicional
    app.config.from_object(Config)

    # Inicializar base de datos
    with app.app_context():
        init_db(app)

    # Registrar rutas (blueprints)
    #app.register_blueprint(root_bp)
    app.register_blueprint(chatbot_bp, url_prefix='/api')
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(modes_bp, url_prefix='/modes')
    app.register_blueprint(minutes_bp, url_prefix='/api')
    app.register_blueprint(elevenlabs_bp, url_prefix='/tts')
    app.register_blueprint(audio_bp, url_prefix='/api')
    # Registrar el blueprint del frontend
    app.register_blueprint(frontend_bp)
    # Eventos de cierre para la base de datos
    app.teardown_appcontext(close_database_connection)

    return app


if __name__ == "__main__":
    app = create_app()
    FlaskInjector(app=app, modules=[configure])
    app.run(debug=Config.DEBUG, host=Config.HOST, port=Config.PORT)
