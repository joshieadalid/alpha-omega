import logging
from typing import Any
from injector import inject

# Configurar logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s [%(levelname)s] %(message)s')
logger = logging.getLogger(__name__)

class ScriptExecutor:
    @inject
    def __init__(self, openai_service, jira_client):
        """
        Inicializa el ejecutor con los clientes necesarios.
        :param openai_service: Servicio de OpenAI.
        :param jira_client: Cliente de Jira.
        """
        self.openai_service = openai_service
        self.jira_client = jira_client
        self.context = {
            'jira': jira_client,
            'result': None,  # Espacio para almacenar el resultado de ejecución
        }

    def execute_prompt_script(self, prompt: str) -> Any:
        """
        Genera y ejecuta un script basado en el prompt dado, devolviendo el resultado.
        :param prompt: Texto que describe el script a generar.
        :return: Resultado de la ejecución del script.
        """
        # Generar el script a partir del servicio OpenAI
        script: str = self.openai_service.generate_script(prompt)
        python_script: str = self.openai_service.extract_code(script, language='python')

        logger.info(f"""Script a ejecutar:
        ------------------
        {python_script}
        ------------------
        """)

        # Ejecutar el script en el contexto inicializado
        try:
            exec(python_script, self.context)
        except Exception as e:
            logger.exception("Error al ejecutar el script generado.")
            raise e

        return self.context.get('result')
