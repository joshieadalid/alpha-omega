from injector import inject


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

    def execute_prompt_script(self, prompt: str) -> any:
        """
        Genera y ejecuta un script basado en el prompt dado, devolviendo el resultado.
        :param prompt: Texto que describe el script a generar.
        :return: Resultado de la ejecución del script.
        """
        # Generar el script a partir del servicio OpenAI
        script: str = self.openai_service.generate_script(prompt)
        python_script: str = self.openai_service.extract_code(script, language='python')

        print(f"""Script a ejecutar:
        ------------------
        {python_script}
        ------------------
        """)

        # Ejecutar el script en el contexto inicializado
        exec(python_script, self.context)
        return self.context.get('result')
