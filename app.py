from flask import Flask

from blueprints.audio_bp import audio_bp
from blueprints.minutes_bp import minutes_bp
from config import Config

# Blueprints
from blueprints.root import root_bp
from blueprints.chatbot_bp import chatbot_bp
from blueprints.auth_bp import auth_bp
from blueprints.modes_bp import modes_bp

# Servicios
from services.db_service import init_db, close_database_connection
from blueprints.elevenlabs_bp import elevenlabs_bp

def create_app():
    app = Flask(__name__)

    # Configuración adicional
    app.config.from_object(Config)

    # Inicializar base de datos
    with app.app_context():
        init_db(app)

    # Registrar rutas (blueprints)
    app.register_blueprint(root_bp)
    app.register_blueprint(chatbot_bp, url_prefix='/api')
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(modes_bp, url_prefix='/modes')
    app.register_blueprint(minutes_bp, url_prefix='/api')
    app.register_blueprint(elevenlabs_bp, url_prefix='/tts')  # Nuevo Blueprint
    app.register_blueprint(audio_bp, url_prefix='/api')
    # Eventos de cierre para la base de datos
    app.teardown_appcontext(close_database_connection)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=Config.DEBUG, host=Config.HOST, port=Config.PORT)
