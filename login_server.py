from flask import Flask, request, jsonify
from database.login_database import init_db, hash_password, check_password
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}}, supports_credentials=True)

# Inicializa la base de datos
init_db()

@app.route('/api/register', methods=['POST'])
def register():
    data = request.get_json()
    email = data.get('email')
    username = data.get('username')
    password = hash_password(data.get('password'))

    try:
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO users (email, password, username) VALUES (?, ?, ?)',
                       (email, password, username))
        conn.commit()
        return jsonify({"message": "Usuario registrado exitosamente"}), 201
    except sqlite3.IntegrityError:
        return jsonify({"error": "El correo ya está registrado"}), 400
    finally:
        conn.close()

@app.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    # Abre la conexión a la base de datos
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    # Recupera `id`, `username` y `password` del usuario
    cursor.execute('SELECT id, username, password FROM users WHERE email = ?', (email,))
    user = cursor.fetchone()
    conn.close()

    if user and check_password(user[2], password):  # Verifica la contraseña
        return jsonify({
            "message": "Inicio de sesión exitoso",
            "user_id": user[0],
            "user_name": user[1]  # Incluye el nombre del usuario en la respuesta
        }), 200

    # Si las credenciales son incorrectas, devuelve un error
    return jsonify({"error": "Credenciales incorrectas"}), 401


if __name__ == "__main__":
    app.run(debug=True, host="localhost")

