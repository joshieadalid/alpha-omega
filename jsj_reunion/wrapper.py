from dotenv import load_dotenv
import os
from jira import JIRA

class JiraWrapper:
    def __init__(self):
        self._load_env()
        self._connect_to_jira()

    def _load_env(self):
        load_dotenv()
        self.username = os.getenv("ATLASSIAN_USERNAME")
        self.api_key = os.getenv("ATLASSIAN_API_KEY")
        self.domain = os.getenv("DOMAIN")

        if not all([self.username, self.api_key, self.domain]):
            raise EnvironmentError("Faltan variables de entorno necesarias.")

    def _connect_to_jira(self):
        self.jira = JIRA(
            server=f"https://{self.domain}.atlassian.net",
            basic_auth=(self.username, self.api_key)
        )

    def __getattr__(self, name):
        """
        Delegar cualquier llamada de método no definido explícitamente al objeto JIRA.
        """
        return getattr(self.jira, name)


if __name__ == "__main__":
    try:
        jira_wrapper = JiraWrapper()

        # Crear un proyecto (usa los métodos de la API de JIRA directamente)
        # project_key = "DEATH2JOHN"
        # project_name = "Garfield"
        # project = jira_wrapper.create_project(
        #    key=project_key,
        #    name=project_name,
        # )
        # print(f"Proyecto creado: {project}")

        # Eliminar un proyecto
        # project_id = "KILLDUCK"
        jira_wrapper.delete_project('TMT')
        # print(f"Proyecto '{project_id}' eliminado correctamente.")

        # Listar proyectos
        
        # Crear el issue
        #issue_data = {
        #    'project': {"key": 'TMT'},
        #    'summary': 'Tomate peligroso',
        #    'description': 'Pinguinos de Palmer',
        #    'issuetype': {'name': 'Bug'}  # Tipo de issue: Bug, Task, etc.
        #}
        #print(jira_wrapper.create_issue(fields=issue_data))

        # Borrar issue (TODO)
        # print(jira_wrapper.issue('TMT-5').delete())

        # Asignar a Josué
        #print(jira_wrapper.assign_issue('TMT-6', 'Josué'))  # Usar accountId

        # Transition issue
        # Obtener las transiciones disponibles para el issue
        # Transiciones disponibles:
        # ID: 11, To Do
        # ID: 21, In Progress
        # ID: 31, Done

        #transitions = jira_wrapper.transitions('TMT-6')  # Cambia 'TMT-6' por el key de tu issue
        #jira_wrapper.transition_issue('TMT-6', 21)



    except Exception as e:
        print(f"Error: {e}")
