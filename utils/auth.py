from flask import request, jsonify
import jwt
from functools import wraps
from flask import current_app

def jwt_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        token = request.headers.get('Authorization')
        print(f"Authorization header received: {token}")
        if not token:
            return jsonify({'message': 'Token is missing'}), 401
        try:
            if token.startswith("Bearer "):
                token = token.split(" ")[1]
            jwt.decode(token, current_app.config['SECRET_KEY'], algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            return jsonify({'message': 'Token has expired'}), 401
        except jwt.InvalidTokenError:
            return jsonify({'message': 'Invalid token'}), 401
        return f(*args, **kwargs)
    return decorated_function