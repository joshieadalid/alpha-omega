from datetime import datetime, timedelta, timezone

import jwt
from flask import Blueprint, request, jsonify, current_app
from werkzeug.security import generate_password_hash, check_password_hash

from authentication.models.user import User
from app import db  # Asegúrate de inicializar `db` en tu aplicación principal

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    # Validación de datos
    if not username or not password:
        return jsonify({'error': 'Missing username or password'}), 400

    # Hash de contraseña
    hashed_password = generate_password_hash(password)

    # Crear usuario
    try:
        new_user = User(username=username, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return jsonify({'message': 'User registered successfully!'}), 201
    except Exception as e:
        db.session.rollback()  # Revertir cambios en caso de error
        return jsonify({'error': f'Error registering user: {str(e)}'}), 400


@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    # Validación de datos
    if not username or not password:
        return jsonify({'error': 'Missing username or password'}), 400

    # Buscar usuario en la base de datos
    user = User.query.filter_by(username=username).first()

    # Verificar contraseña
    if user and check_password_hash(user.password, password):
        # Generar JWT
        token = jwt.encode(
            {'id': user.id, 'username': user.username, 'exp': datetime.now(timezone.utc) + timedelta(hours=1)},
            current_app.config['SECRET_KEY'], algorithm='HS256')
        return jsonify({'token': token}), 200

    # Credenciales inválidas
    return jsonify({'error': 'Invalid username or password'}), 401
