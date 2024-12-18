import os
import subprocess
from requests.auth import HTTPBasicAuth
from result import *

from jsj_reunion.fun_args import execute_function
from jsj_reunion.wrapper import JiraWrapper
from typing import TypedDict


# Configuración de Atlassian
atlassian_username = os.getenv("ATLASSIAN_USERNAME")
atlassian_api_key = os.getenv("ATLASSIAN_API_KEY")
auth = HTTPBasicAuth(atlassian_username, atlassian_api_key)


def execute_jira_action(action_code: int, user_message: str = None):
    """
    Ejecuta una acción específica en Jira basada en el código de acción.
    """
    print("Ejecutando acción con código:", action_code)
    try:
        if action_code == 1:
            return execute_js("create-project.js", user_message)
        elif action_code == 2:
            return execute_js("delete-project.js", user_message)
        elif action_code == 3:
            return execute_js("get-projects.js", user_message)
        else:
            raise ValueError(f"Código de acción no válido: {action_code}")
    except Exception as e:
        raise Exception(f"Error ejecutando acción en Jira: {e}")


def execute_js(js_filename, user_message) -> Result[str, str]:
    """
    Ejecuta un script de Node.js con los parámetros proporcionados.
    """
    try:
        result = subprocess.run(
            ["node", f"JSJira/{js_filename}", user_message],
            capture_output=True,
            text=True
        )
        if result.returncode == 0:
            return Ok(result.stdout)
        else:
            return Err(result.stderr)
    except Exception as e:
        return Err(str(e))


def process_and_execute_actions(actions_json):
    """
    Procesa un JSON de acciones y las ejecuta una por una.

    :param actions_json: Lista de acciones en formato JSON.
    :return: Lista de resultados de la ejecución de cada acción.
    """
    print("Acciones pendientes: ", actions_json)
    results = []
    for action in actions_json:
        try:
            result = execute_jira_action(action["action_id"], action.get("description", ""))
            results.append({
                "action_id": action["action_id"],
                "description": action.get("description", ""),
                "result": result
            })
        except Exception as e:
            results.append({
                "action_id": action["action_id"],
                "description": action.get("description", ""),
                "error": str(e)
            })
    return results




def process_actions(actions_json, module_name: str='jsj_reunion.wrapper', class_name: str='JiraWrapper'):
    """
    Procesa una lista de acciones y ejecuta las funciones dinámicamente.

    Args:
        actions_json (list[Action]): Lista de acciones a procesar.
        module_name (str): Nombre del módulo donde está la clase.
        class_name (str): Nombre de la clase que contiene las funciones.

    Returns:
        list: Resultados de la ejecución de las acciones.
    """
    resultados = []
    for action in actions_json:
        try:
            print('Acción actual: ', action)
            # Usar execute_function para procesar cada acción
            resultado = execute_function(module_name, class_name, action)

            print("Resultado: ", resultado)
            resultados.append(str(resultado))
        except Exception as e:
            # Manejar errores y continuar con la siguiente acción
            resultados.append({"error": str(e)})
    return resultados


