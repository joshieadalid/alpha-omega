from flask import Flask
from config import Config

# Blueprints
from blueprints.chatbot_bp import chatbot_bp
from blueprints.auth_bp import auth_bp
from blueprints.modes_bp import modes_bp

# Servicios
from services.db_service import close_database_connection

def create_app():
    app = Flask(__name__)
    app.secret_key = Config.SECRET_KEY

    # Configuración adicional
    app.config.from_object(Config)

    # Registrar rutas (blueprints)
    app.register_blueprint(chatbot_bp, url_prefix='/api')
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(modes_bp, url_prefix='/modes')

    # Eventos de cierre para la base de datos
    app.teardown_appcontext(close_database_connection)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=Config.DEBUG, host=Config.HOST, port=Config.PORT)
