# services/openai_service.py
import io
import json

from werkzeug.datastructures import FileStorage


class OpenAIService:
    """Servicio que interactúa con la API de OpenAI."""

    def __init__(self, openai_client, model_type: str):
        self.openai_client = openai_client
        self.model_type = model_type

    def transcribe_audio(self, audio_file: FileStorage) -> str:
        # Validación del archivo
        if not audio_file or not isinstance(audio_file, FileStorage):
            raise ValueError("No se proporcionó un archivo válido")

        if not audio_file.filename.endswith(".ogg"):
            print(audio_file.filename)
            raise ValueError("El archivo no es un OGG válido")

        try:
            # Procesar el archivo
            audio_bytes = audio_file.read()
            audio_io = io.BytesIO(audio_bytes)
            audio_io.name = audio_file.filename

            # Enviar a OpenAI
            transcription = self.openai_client.audio.transcriptions.create(model="whisper-1", language="es",
                                                                           file=audio_io)

            return transcription.text
        except Exception as e:
            raise Exception(f"Error al transcribir el archivo: {str(e)}")

    def extract_json(self, text):
        try:
            start_index = text.find("```json") + len("```json")
            end_index = text.find("```", start_index)
            json_string = text[start_index:end_index].strip()
            return json.loads(json_string)
        except Exception as error:
            return {"error": str(error)}

    def extract_python(self, text):
        try:
            start_index = text.find("```python") + len("```python")
            end_index = text.find("```", start_index)
            python_code = text[start_index:end_index].strip()
            return python_code
        except Exception as error:
            return {"error": str(error)}

    def generate_script(self, text: str) -> str:
        """
        Genera un script Python a partir del texto proporcionado y lo devuelve como código.
        """
        # prompt = {
        #    "role": "system",
        #    "content": """Eres un asistente experto en generar código Python que interactúe con la API de la biblioteca del cliente de Jira.
        #        El objeto que gestionará la conexión con la API es:
        #        jira = JiraClient()
        #        - No necesitas importar el cliente.
        #        create_project no necesita summary. Solo el key y el name.
        #        - Si necesitas usar create_issue(fields: dict[str, Any] | None = None, prefetch: bool = True, **fieldargs) → Issue.
        #        - fields es un objeto, con atributos project, summary, description, issuetype, project es un objeto con atributo key. issuetype es un objeto con atributo name.
        #        - create_issue no las asigna automáticamente, para eso necesitas assign_issue:  assign_issue(issue: int | str, assignee: str | None) → bool[source]
        #        - El resultado final lo guardarás en la variable result.
        #        - Para listar todos los usuarios, el query debe tener un espacio.
        #        - Para borrar un issue primero obtenlo y aplícale delete, por ejemplo: jira.issue('ISSUE_KEY').delete())
        #        """
        # }
        prompt = {"role": "system", "content": """
                Eres un asistente experto en generar código Python para interactuar con la API del cliente de Jira.
                El objeto que se utilizará para gestionar la conexión con la API es:
                    jira = JiraClient()
                **No necesitas importar el cliente.**
    
                ### Detalles importantes:
                1. **Creación de proyectos:**
                - Utiliza create_project con los atributos key y name. No es necesario incluir summary.
    
                2. **Creación de issues:**
                - Utiliza create_issue(fields: dict[str, Any] | None = None, prefetch: bool = True, **fieldargs) → Issue.
                - El objeto fields debe incluir los siguientes atributos obligatorios:
                    - project: Un objeto con el atributo key.
                    - summary: Un resumen breve del issue.
                    - description: Una descripción detallada del issue.
                    - issuetype: Un objeto con el atributo name que define el tipo de issue.
                - Nota: create_issue no asigna automáticamente los issues. Para ello, utiliza el método assign_issue.
    
                3. **Asignación de issues:**
                - Utiliza assign_issue(issue: int | str, assignee: str | None) → bool.
                - El parámetro issue es el identificador (ID o clave) del issue.
                - El parámetro assignee es el nombre del usuario al que se asignará el issue.
    
                4. **Listar usuarios:**
                - Para listar todos los usuarios, realiza un query que contenga un espacio en blanco como criterio.
    
                5. **Eliminación de issues:**
                - Para borrar un issue, primero obtén el issue utilizando su clave, y luego aplica el método delete().
                - Ejemplo:
                    jira.issue('ISSUE_KEY').delete()
                6. **Almacenamiento de resultados:**
                - Guarda el resultado final de cualquier operación en la variable result.
                """}

        user_message = {"role": "user",
            "content": f"""Genera el código Python necesario para ejecutar las acciones a partir del siguiente texto: '{text}'
                 **Estructura esperada:**
                    - Asegúrate de que el código sea funcional y siga las reglas de interacción con la API del cliente de Jira.
                     - Todos los resultados deben almacenarse en una variable llamada result."""}

        try:
            # Generar el script con la API de OpenAI
            response = self.openai_client.chat.completions.create(model=self.model_type,
                # Puedes cambiar el modelo según sea necesario
                messages=[prompt, user_message])

            # Obtener el código generado
            generated_script = response.choices[0].message.content.strip()
            return generated_script  # Devolver el código generado

        except Exception as e:
            raise Exception(f"Error al generar el script: {e}")

    def format_api_response(self, api_json_response: str) -> str:
        system_prompt = {"role": "system",
            "content": """Traduce las respuestas en formato JSON provenientes de la API REST de Jira a un formato de texto plano y no markdown, comprensible para cualquier persona, explicando los datos relevantes de manera clara y estructurada, omitiendo detalles técnicos innecesarios. Debe ser al estilo de mensaje de debug, impersonal. Como si un sistema estuviera informando acerca de lo ocurrido. Solo mencionas los datos, sin interpretarlos."""}

        user_instruction = {"role": "user",
            "content": f"Este es un JSON con la respuesta de una API tras una transacción. Por favor, analiza la respuesta y proporciona un resumen claro y breve que explique qué significa la respuesta y cuál es el estado o resultado de la transacción. Ignora detalles técnicos o atributos secundarios. Solo indica de manera comprensible qué ocurrió con la transacción (por ejemplo, si fue exitosa, fallida, pendiente, o algún detalle relevante). Aquí está el JSON: {api_json_response}."}
        try:
            chat_response = self.openai_client.chat.completions.create(model=self.model_type,
                # Puedes cambiar el modelo según sea necesario
                messages=[system_prompt, user_instruction])

            formated_text = chat_response.choices[0].message.content.strip()
            return formated_text  # Devolver el texto generado
        except Exception as e:
            raise Exception(f"Error al generar el script: {e}")
