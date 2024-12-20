import io

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

    @staticmethod
    def extract_code(text, language):
        """
        Extracts a code block for a specified language from a given text.

        Parameters:
            text (str): The text containing the code block.
            language (str): The programming language of the code block (e.g., 'python', 'html', etc.).

        Returns:
            str: The extracted code block or an error message if extraction fails.
        """
        try:
            start_marker = f"```{language}"
            start_index = text.find(start_marker) + len(start_marker)
            end_index = text.find("```", start_index)
            if start_index == -1 or end_index == -1:
                raise ValueError(f"No code block found for language '{language}'.")
            code_block = text[start_index:end_index].strip()
            return code_block
        except Exception as error:
            return {"error": str(error)}

    def generate_script(self, text: str) -> str:
        """
        Genera un script Python a partir del texto proporcionado y lo devuelve como código.
        """

        prompt = {"role": "system", "content": """
                Eres un asistente experto en generar código Python para interactuar con la API del cliente de Jira.
                El objeto que se utilizará para gestionar la conexión con la API es:
                
                Gestiona las excepciones de forma que aunque un fragmento del código haya fallado, pueda seguir con lo demás. El objetivo es tener la variable `result`.
                    jira, una instancia de JIRA, ya inicializada
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
                    - issuetype: Un objeto con el atributo `name` que define el tipo de issue como 'Bug', 'Story', 'Task', entre otros.
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

    def minute_text(self, text: str, timestamp) -> str:
        """
        Genera una minuta con el texto de la reunión.
        """
        prompt = {"role": "system", "content": """
                Eres un redactor experto en redactar minutas empresariales de la metodología de Scrum.
                """}

        user_message = {"role": "user", "content": f"""Redacta la minuta para el día {timestamp} acerca de lo que se habló en esta reunión.
                        1. Detalles básicos

    Fecha de la reunión.
    Hora de inicio y fin.
    Participantes (nombres y roles en el equipo: Scrum Master, Product Owner, Developers).

2. Objetivo de la reunión

    Tipo de reunión (Daily Scrum, Sprint Planning, Sprint Review, Sprint Retrospective).
    Propósito o metas específicas.

3. Resumen del progreso

    Daily Scrum:
        Qué se completó desde la última reunión.
        Qué se planea completar antes de la próxima reunión.
        Impedimentos o bloqueos.
    Sprint Planning:
        Historias de usuario seleccionadas del backlog.
        Objetivo del sprint.
        Tareas asignadas.
    Sprint Review:
        Trabajo completado y no completado.
        Feedback del Product Owner y/o stakeholders.
    Sprint Retrospective:
        Qué funcionó bien.
        Qué no funcionó.
        Acciones de mejora.

4. Decisiones importantes

    Cambios en prioridades.
    Soluciones a problemas discutidos.
    Compromisos o acuerdos.

5. Impedimentos y bloqueos

    Problemas no resueltos que afectan al equipo.
    Quién es responsable de resolverlos.

6. Próximos pasos

    Acciones asignadas con responsables y fechas límite.
    Planes específicos para la próxima reunión o sprint.

7. Notas adicionales

    Comentarios o temas fuera del alcance que requieran seguimiento posterior.
    Observaciones relevantes sobre el equipo o el proceso.

Mantén la minuta clara y concisa, evitando detalles irrelevantes. Su propósito principal es servir como referencia para el equipo y garantizar que todos estén alineados.

                        A continuación, la transcripción:
{text}."""}

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

    def minute_to_html(self, text: str) -> str:
        prompt = {"role": "system",
                  "content": f"Eres un sistema que genera un reporte de HTML semántico y con CSS BEM incrustado en el mismo archivo; para una minuta en texto plano."}

        user_message = {"role": "user", "content": f"Genera el reporte para la siguiente minuta: {text}"}

        try:
            response = self.openai_client.chat.completions.create(model='gpt-4o-mini',
                                                                  messages=[prompt, user_message]).choices[
                0].message.content.strip()
            html_code = self.extract_code(text=response, language='html')
            return html_code
        except Exception as e:
            raise Exception(f'Error al formatear la minuta en HTML.')
