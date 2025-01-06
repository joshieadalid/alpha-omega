from flask import Flask
from flask_injector import FlaskInjector
from flask_cors import CORS  # Importar CORS

from blueprints.audio_bp import audio_bp
from blueprints.auth_bp import auth_bp
from blueprints.chatbot_bp import chatbot_bp
from blueprints.elevenlabs_bp import elevenlabs_bp
from blueprints.minutes_bp import minutes_bp
from blueprints.modes_bp import modes_bp
# Blueprints
from blueprints.root import root_bp
from config import Config
# Contenedor de dependencias
from di_container import configure
# Servicios
from services.database_manager import db_manager


def create_app():
    app: Flask = Flask(__name__)

    # Configuración adicional
    app.config.from_object(Config)

    # Inicializar base de datos
    db_manager.init_app(app)

    # Habilitar CORS para todas las rutas
    CORS(app)  # Permitir solicitudes desde cualquier origen

    # Registrar rutas (blueprints)
    app.register_blueprint(root_bp, url_prefix='/')
    app.register_blueprint(chatbot_bp, url_prefix='/api')
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(modes_bp, url_prefix='/modes')
    app.register_blueprint(minutes_bp, url_prefix='/api')
    app.register_blueprint(elevenlabs_bp, url_prefix='/tts')
    app.register_blueprint(audio_bp, url_prefix='/api')
    # Registrar el blueprint del frontend
    # app.register_blueprint(frontend_bp)
    # Eventos de cierre para la base de datos
    app.teardown_appcontext(db_manager.close_connection)

    return app


if __name__ == "__main__":
    app = create_app()
    FlaskInjector(app=app, modules=[configure])
    app.run(debug=Config.DEBUG, host=Config.HOST, port=Config.PORT)
