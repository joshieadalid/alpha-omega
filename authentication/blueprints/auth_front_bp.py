import logging
from flask import Blueprint, request, jsonify
from injector import inject
from werkzeug.exceptions import BadRequest, Unauthorized
from authentication.services.user_service import UserService

# Configurar el logger
logging.basicConfig(level=logging.INFO, format='%(asctime)s [%(levelname)s] %(message)s')
logger = logging.getLogger(__name__)

auth_front_bp = Blueprint('auth_bp', __name__)


@auth_front_bp.route('/register', methods=['POST'])
@inject
def register(user_service: UserService):
    """
    Endpoint para registrar un nuevo usuario.
    """
    logger.info("Solicitud de registro recibida")

    try:
        data = request.get_json()
        if not data:
            logger.error("Cuerpo de la solicitud vacío o no es JSON")
            raise BadRequest("El cuerpo de la solicitud debe ser JSON válido.")
    except Exception as e:
        logger.error(f"Error al parsear JSON en la solicitud: {e}")
        raise BadRequest("Formato JSON inválido.")

    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    if not username or not email or not password:
        logger.warning(f"Datos incompletos: username={username}, email={email}, password={'presente' if password else 'ausente'}")
        raise BadRequest("Se requieren 'username', 'email' y 'password'.")

    logger.info(f"Intentando registrar usuario: username={username}, email={email}")
    try:
        user = user_service.add_user(username, email, password)
        logger.info(f"Usuario registrado exitosamente: username={username}, email={email}, id={user.id}")
        return jsonify({"message": "Usuario registrado exitosamente", "user": user.to_dict()}), 201
    except ValueError as e:
        logger.error(f"Error al registrar usuario: {e}")
        return jsonify({"error": str(e)}), 400


@auth_front_bp.route('/login', methods=['POST'])
@inject
def login(user_service: UserService):
    """
    Endpoint para iniciar sesión.
    """
    logger.info("Solicitud de inicio de sesión recibida")

    try:
        data = request.get_json()
        if not data:
            logger.error("Cuerpo de la solicitud vacío o no es JSON")
            raise BadRequest("El cuerpo de la solicitud debe ser JSON válido.")
    except Exception as e:
        logger.error(f"Error al parsear JSON en la solicitud: {e}")
        raise BadRequest("Formato JSON inválido.")

    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        logger.warning(f"Datos incompletos: email={email}, password={'presente' if password else 'ausente'}")
        raise BadRequest("Se requieren 'email' y 'password'.")

    logger.info(f"Intentando autenticar usuario: email={email}")
    user = user_service.authenticate_user(email, password)

    if not user:
        logger.warning(f"Autenticación fallida para email={email}")
        raise Unauthorized("Credenciales incorrectas.")

    logger.info(f"Usuario autenticado exitosamente: email={email}, id={user.id}")
    return jsonify({"message": "Inicio de sesión exitoso", "user_id": user.id, "username": user.username}), 200
