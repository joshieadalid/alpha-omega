import io
import os
import subprocess

import openai
from dotenv import load_dotenv
from flask import Flask, request, jsonify, render_template, redirect, url_for
from pydub import AudioSegment
from requests.auth import HTTPBasicAuth

load_dotenv()

app = Flask(__name__)

# Configura tu clave de API de OpenAI
openai.api_key = os.environ.get("API_KEY_OPENAI")
atlassian_username = os.environ.get("ATLASSIAN_USERNAME")
atlassian_api_key = os.environ.get("ATLASSIAN_API_KEY")

if not openai.api_key or not atlassian_username or not atlassian_api_key:
    print("Error: Una o más claves de API no están configuradas.")
    exit(1)

# Genera el header de autorización en Base64
auth = HTTPBasicAuth(atlassian_username, atlassian_api_key)
configHeaders = {"Authorization": f"Basic {auth}", "Content-Type": "application/json"}


@app.route('/')
def index():
    return render_template('chatbot.html')



AI_personality_conf = ("Eres un asistente y secretario con 30 años de experiencia en el desarrollo de proyectos de "
                       "software y tecnología de la información. Tu objetivo es ayudar a las empresas y ayudar a los "
                       "clientes para elegir funciones en jira y responder preguntas casuales , tu nombre es Jarvis")

Super_precision = "Eres un modulo de un programa que sigue las instrucciones al pie de la letra"


# Ruta para manejar el chatbot y los comandos relacionados con Jira
@app.route("/chatbot", methods=["POST"])
def chat():
    global output
    print("Recibida solicitud en /chatbot")

    # Verifica si el contenido es JSON (texto) o un archivo de audio
    if request.content_type == 'application/json':
        data = request.get_json()
        user_message = data.get("message", "") if data else ""
    else:
        user_message = ""

    # Si no se recibe un mensaje de texto, intenta obtener el archivo de audio
    if not user_message:
        if 'audio' in request.files:
            audio_file = request.files['audio']
            try:
                # Convertir el archivo FileStorage a BytesIO para compatibilidad con OpenAI
                audio = AudioSegment.from_file(audio_file)
                audio_wav = io.BytesIO()
                audio.export(audio_wav, format="wav")
                audio_wav.name = "recording.wav"
                audio_wav.seek(0)  # Darle un nombre al archivo
                # Usa Whisper para transcribir el audio
                transcription = openai.audio.transcriptions.create(model="whisper-1", file=audio_wav,
                    response_format="text")
                user_message = transcription
                print(f"Transcripción del audio: {user_message}")
            except Exception as e:
                print("Error al transcribir el audio:", e)
                return jsonify({"error": "Error al transcribir el audio"}), 500
        else:
            return jsonify({"error": "No se recibió ni mensaje ni archivo de audio"}), 400

    print(f"Mensaje del usuario: {user_message}")

    formatted_message = (
        f"Debes verificar si el mensaje siguiente se asocia a alguna               de las siguientes peticiones en Jira: "
        f"1. Crear proyecto, 2. Eliminar proyecto, 3. Obtener                      proyectos, 4. Obtener usuarios. "
        f"Si se asocia a alguna, devuelve únicamente y exclusivamente el         número de la opción, no des contexto ni otro tipo de dato, en cambio "
        f"si no se asocia a ninguna, responde 0. El mensaje es el siguiente: {user_message}")

    # Usa GPT para responder al mensaje del usuario
    try:
        response = openai.chat.completions.create(model="gpt-3.5-turbo",  # Usa el modelo correcto
            messages=[{"role": "system", "content": AI_personality_conf},
                {"role": "user", "content": formatted_message}])

        bot_reply = response.choices[0].message.content
        print(f"Respuesta del bot: {bot_reply}")  # Muestra la respuesta del bot

        if bot_reply.strip() == "0":
            final_response = openai.chat.completions.create(model="gpt-3.5-turbo",  # Usa el modelo correcto
                messages=[{"role": "system", "content": AI_personality_conf},
                    {"role": "user", "content": user_message}])
            output = final_response.choices[0].message.content

        if bot_reply.strip() == "1":
            print("Ejecutando script de Node.js para crear el proyecto en Jira...")
            try:
                # Llama al script de Node.js
                result = subprocess.run(["node", "JSJira/create-project.js", user_message],
                    capture_output=True, text=True)
                # Captura el resultado o el error de la ejecución
                if result.returncode == 0:
                    output = f"Proyecto creado con éxito: {result.stdout}"
                else:
                    output = f"Error al crear el proyecto en Jira: {result.stderr}"
            except Exception as e:
                output = f"Error al ejecutar el script de Node.js: {e}"

            print(f"Respuesta del bot: {output}")

        if bot_reply.strip() == "2":
            print("Ejecutando script de Node.js para eliminar el proyecto en Jira...")
            try:
                # Llama al script de Node.js
                result = subprocess.run(["node", "JSJira/delete-project.js", user_message], capture_output=True,
                    text=True)
                # Captura el resultado o el error de la ejecución
                if result.returncode == 0:
                    output = f"Proyecto eliminado con éxito: {result.stdout}"
            except Exception as e:
                output = f"Error al ejecutar el script de Node.js: {e}"
            print(f"Respuesta del bot: {output}")

        if bot_reply.strip() == "3":
            print("Ejecutando script de Node.js para obtener los proyectos en Jira...")
            try:
                # Llama al script de Node.js
                result = subprocess.run(["node", "JSJira/get-projects.js"], capture_output=True, text=True)
                # Captura el resultado o el error de la ejecución
                if result.returncode == 0:
                    output = f"Proyectos obtenidos con éxito: {result.stdout}"
                else:
                    output = f"Error al obtener los proyectos en Jira: {result.stderr}"
            except Exception as e:
                output = f"Error al ejecutar el script de Node.js: {e}"
            print(f"Respuesta del bot: {output}")

        if bot_reply.strip() == "4":
            print("Ejecutando script de Node.js para obtener los usuarios en Jira...")
            try:
                # Llama al script de Node.js
                result = subprocess.run(["node", "JSJira/get-users.js"], capture_output=True, text=True)
                # Captura el resultado o el error de la ejecución
                if result.returncode == 0:
                    output = f"Usuarios obtenidos con éxito: {result.stdout}"
                else:
                    output = f"Error al obtener los usuarios en Jira: {result.stderr}"

            except Exception as e:
                output = f"Error al ejecutar el script de Node.js: {e}"
            print(f"Respuesta del bot: {output}")

        return jsonify({"reply": output})
    except Exception as e:
        print(f"Error en la API de OpenAI: {e}")  # Muestra el error específico
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    print("Iniciando servidor Flask...")
    app.run(host='0.0.0.0', port=8080)

# Haz un proyecto en Jira con el nombre VATO LOCO e id VL1
