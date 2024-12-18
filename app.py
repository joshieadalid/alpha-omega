import argparse

from dotenv import load_dotenv
from flask import Flask, request, render_template, redirect, url_for
from controllers.chatbot_controller import chatbot_route

# Cargar variables de entorno
load_dotenv()

app = Flask(__name__)

# Registrar rutas
app.register_blueprint(chatbot_route)

# Rutas estáticas
@app.route('/')
def login():
    return render_template('index.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/menu')
def menu():
    return render_template('menu.html')

@app.route('/modo_reunion')
def modo_reunion():
    return render_template('modo_reunion.html')

@app.route('/modo_comandos')
def modo_comandos():
    return render_template('modo_comandos.html')


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Ejecutar el servidor Flask.")
    parser.add_argument("--port", type=int, default=8080, help="El puerto en el que se ejecutará el servidor.")
    args = parser.parse_args()

    print("Iniciando servidor Flask...")
    app.run(debug=True, host='0.0.0.0', port=args.port, ssl_context=('certs/cert.pem', 'certs/key.pem'))