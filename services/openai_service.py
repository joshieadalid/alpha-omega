import io
import os
import json
import openai
from result import *
from werkzeug.datastructures import FileStorage

from services.action_t import Action

# Configuración de OpenAI
openai.api_key = os.getenv("API_KEY_OPENAI")

# ID de tu modelo ajustado
FINE_TUNED_MODEL_ID = "gpt-3.5-turbo"

# Personalidad del asistente y módulo de precisión
AI_personality_conf = """Eres un asistente y secretario con 30 años de experiencia en el desarrollo de proyectos de 
software y tecnología de la información. Tu objetivo es ayudar a las empresas y ayudar a los clientes para elegir 
funciones en jira y responder preguntas casuales , tu nombre es Jarvis"""

super_precision = "Eres un modulo de un programa que sigue las instrucciones al pie de la letra"


def transcribe_audio(audio_file: FileStorage) -> Result[str, str]:
    # Validación del archivo
    if not audio_file or not isinstance(audio_file, FileStorage):
        return Err("No se proporcionó un archivo válido")

    if not audio_file.filename.endswith(".wav"):
        print(audio_file.filename)
        return Err("El archivo no es un WAV válido")

    try:
        # Procesar el archivo
        audio_bytes = audio_file.read()
        audio_io = io.BytesIO(audio_bytes)
        audio_io.name = audio_file.filename

        # Enviar a OpenAI
        transcription = openai.audio.transcriptions.create(model="whisper-1", language="es", file=audio_io)

        return Ok(transcription.text)
    except Exception as e:
        return Err(str(e))


def process_message(user_message):
    """
    Procesa el mensaje de texto: obtiene la respuesta de OpenAI y ejecuta acciones en Jira.
    """
    if not user_message:
        raise ValueError("El mensaje de texto está vacío")

    response = get_action_code(user_message)
    return response


def get_action_code(user_message) -> int:
    formatted_message = f"""
        Verifica si el mensaje se asocia a alguna de estas peticiones en Jira:
        1. Crear proyecto
        2. Eliminar proyecto
        3. Obtener proyectos
        4. Obtener usuarios
        No digas nada mas que el código. Si se asocia, responde únicamente con el número de la opción. Si no, responde 0.
        Mensaje: {user_message}
        """

    try:
        # Usar el modelo ajustado (fine-tuned)
        response = openai.chat.completions.create(model=FINE_TUNED_MODEL_ID,
                                                  messages=[{"role": "system", "content": AI_personality_conf},
                                                            {"role": "user", "content": formatted_message}])
        return int(response.choices[0].message.content)
    except Exception as e:
        raise Exception(f"Error en la API de OpenAI: {e}")


# Modo reunión

# Tabla de acciones definidas
ACTION_TABLE = {1: "crear proyecto", 2: "eliminar proyecto", 3: "obtener proyectos", 4: "obtener usuarios"}


def format_actions_to_json(actions_text: str) -> list[Action]:
    """
    Convierte el texto de acciones en una lista JSON estructurada.
    """
    actions: list[Action] = []
    try:
        lines = actions_text.strip().split("\n")
        for line in lines:
            # Verifica que la línea comience con "-"
            if line.strip().startswith("-"):
                # Divide la línea para extraer el ID y la descripción
                parts = line.split(": ", 2)  # Dividir solo en los dos primeros ":" encontrados
                if len(parts) >= 3:
                    action_id = parts[0].strip().lstrip("- ").split()[0]  # Extrae el ID
                    action_name = parts[1].strip()  # Extrae el nombre de la acción
                    description = parts[2].strip()  # Extrae la descripción

                    # Agrega la acción al resultado
                    actions.append(
                        {"action_id": int(action_id), "action_name": action_name, "description": description})
    except Exception as e:
        raise ValueError(f"Error al formatear las acciones: {e}")
    return actions


def parsear_json(texto) -> dict | list:
    # Remover las comillas de código invertidas y la leyenda "json"
    texto_limpio = texto.replace("```json", "").replace("```", "").strip()
    # Convertir el texto limpio en un objeto JSON
    return json.loads(texto_limpio)


def extract_actions(text) -> list[Action]:
    """
    Extrae acciones a partir de un texto transcrito y las devuelve como una lista de objetos JSON.
    """
    if not text:
        raise ValueError("El texto proporcionado está vacío")

    prompt = {
        "role": "system",
        "content": "Eres un asistente experto en identificar acciones específicas a partir de texto y convertirlas a un formato JSON estructurado."
    }

    user_message = {
        "role": "user",
        "content": f"""
        A partir del siguiente texto, identifica las acciones relevantes como una lista de acciones. En una lista de objetos en JSON. Formato:

        [
            {{
                "function_name": "create_project",
                "args": {{
                    "key":"Mandatory. Must match Jira project key requirements, usually only 2-10 uppercase characters.",
                    "name":"If not specified it will use the key value."
                }}
            }},
            {{
                "function_name": "delete_project",
                "args": {{
                    "pid":"Jira projectID or Project or slug.",
                }}
            }},
            {{
                "function_name": "projects",
                "args": {{
                }}
            }},
            {{
                "function_name": "create_issue",
                "args": {{
                    "fields":{{
                        'project': {{"key": 'TMT'}},
                        'summary': 'Tomate peligroso',
                        'description': 'Pinguinos de Palmer',
                        'issuetype': {{'name': 'Bug'}} # Tipo de issue: Bug, Task, etc.
                    }}
                }}
            }},
            {{
                "function_name": "assign_issue",
                "args": {{
                    'issue':'the issue ID or key to assign',
                    'assignee':'the user to assign the issue to'
                }}
            }},
            {{
                "function_name": "transition_issue",
                "args": {{
                    'issue':'ID or key of the issue to perform the transition on',
                    'transition':'ID or name of the transition to perform (11 To Do, 21 In  Progress, 31 Done)'
                }}
            }},
        ]

        Dada la siguiente información: {text}
        """
    }

    try:
        print("User message: ", text)
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[prompt, user_message]
        )
        # La respuesta ya debería estar en formato JSON si el modelo sigue las instrucciones.
        actions_json = response.choices[0].message.content.strip()
        print("Actions json: ", actions_json)
        data = parsear_json(actions_json)

        print("Respuesta chatgpt: ", data)
        # Validamos y convertimos la respuesta a una lista de diccionarios.
        return data
    except Exception as e:
        raise Exception(f"Error en la API de OpenAI o en el procesamiento de JSON: {e}")


def extract_actions_from_audio(audio_file) -> list[Action]:
    """
    Transcribe el audio y luego extrae las acciones.
    """
    transcription_result: Ok[str] | Err[str] = transcribe_audio(audio_file)

    if isinstance(transcription_result, Err):
        return transcription_result  # Retorna el error directamente si falla la transcripción

    transcription_text = transcription_result.unwrap()  # Extrae el texto si es Ok
    actions_result: list[Action] = extract_actions(transcription_text)

    return actions_result  # Devuelve el resultado de extraer acciones (Ok o Err)
