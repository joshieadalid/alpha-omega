import io
import os
import subprocess

import openai
from dotenv import load_dotenv
from pydub import AudioSegment
from requests.auth import HTTPBasicAuth

# Cargar variables de entorno
load_dotenv()

# Configura tu clave de API de OpenAI y las credenciales de Jira
openai.api_key = os.getenv("API_KEY_OPENAI")
atlassian_username = os.getenv("ATLASSIAN_USERNAME")
atlassian_api_key = os.getenv("ATLASSIAN_API_KEY")

if not openai.api_key or not atlassian_username or not atlassian_api_key:
    raise ValueError("Error: Una o más claves de API no están configuradas.")

# Configuración de autenticación de Jira
auth = HTTPBasicAuth(atlassian_username, atlassian_api_key)
configHeaders = {"Authorization": f"Basic {auth}", "Content-Type": "application/json"}

AI_PERSONALITY_CONF = (
    'Eres un asistente y secretario con 30 años de experiencia en el desarrollo de proyectos de software y tecnología '
    'de la información. Tu objetivo es ayudar a las empresas y a los clientes para elegir funciones en jira y responder preguntas casuales.')


# Función para transcribir audio usando OpenAI Whisper
def transcribir_audio(audio_file):
    try:
        audio = AudioSegment.from_file(audio_file)
        audio_wav = io.BytesIO()
        audio.export(audio_wav, format="wav")
        audio_wav.name = "recording.wav"
        audio_wav.seek(0)
        transcription = openai.Audio.transcriptions.create(model="whisper-1", file=audio_wav, response_format="text")
        return transcription
    except Exception as e:
        raise ValueError(f"Error al transcribir el audio: {e}")


# Función para procesar el mensaje y determinar la acción en Jira
def procesar_mensaje_jira(user_message):
    # Formatea el mensaje del usuario para la consulta
    formatted_message = (
        "Debes verificar si el mensaje siguiente se asocia a alguna de las siguientes peticiones en Jira: "
        "1. Crear proyecto, 2. Eliminar proyecto, 3. Obtener proyectos, 4. Obtener usuarios. "
        "Si se asocia a alguna, devuelve únicamente el número de la opción, no des contexto adicional. "
        f"El mensaje es el siguiente: {user_message}")

    try:
        # Realiza la llamada a la API con la nueva sintaxis
        response = openai.completions.create(model="gpt-3.5-turbo",
                                             messages=[{"role": "system", "content": AI_PERSONALITY_CONF},
                                                       {"role": "user", "content": formatted_message}])
        # Extrae y devuelve la respuesta del modelo
        return response['choices'][0]['message']['content'].strip()
    except Exception as e:
        # Maneja cualquier error de la API
        print(f"Error al procesar el mensaje en OpenAI: {e}")
        return "Error al procesar el mensaje."


# Funciones para ejecutar comandos de Node.js que interactúan con Jira

def crear_proyecto_jira(nombre_proyecto, id_proyecto):
    try:
        result = subprocess.run(["node", "JSJira/create-project.js", nombre_proyecto, id_proyecto], capture_output=True,
                                text=True)
        if result.returncode == 0:
            return f"Proyecto creado con éxito: {result.stdout}"
        else:
            return f"Error al crear el proyecto en Jira: {result.stderr}"
    except Exception as e:
        return f"Error al ejecutar el script de Node.js: {e}"


def eliminar_proyecto_jira(id_proyecto):
    try:
        result = subprocess.run(["node", "JSJira/delete-project.js", id_proyecto], capture_output=True, text=True)
        if result.returncode == 0:
            return f"Proyecto eliminado con éxito: {result.stdout}"
        else:
            return f"Error al eliminar el proyecto en Jira: {result.stderr}"
    except Exception as e:
        return f"Error al ejecutar el script de Node.js: {e}"


def obtener_proyectos_jira():
    try:
        result = subprocess.run(["node", "JSJira/get-projects.js"], capture_output=True, text=True)
        if result.returncode == 0:
            return f"Proyectos obtenidos con éxito: {result.stdout}"
        else:
            return f"Error al obtener los proyectos en Jira: {result.stderr}"
    except Exception as e:
        return f"Error al ejecutar el script de Node.js: {e}"


def obtener_usuarios_jira():
    try:
        result = subprocess.run(["node", "JSJira/get-users.js"], capture_output=True, text=True)
        if result.returncode == 0:
            return f"Usuarios obtenidos con éxito: {result.stdout}"
        else:
            return f"Error al obtener los usuarios en Jira: {result.stderr}"
    except Exception as e:
        return f"Error al ejecutar el script de Node.js: {e}"
