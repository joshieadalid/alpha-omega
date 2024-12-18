import importlib

def execute_function(module_name, class_name, payload):
    """
    Cargar un módulo, instanciar una clase y ejecutar un método dinámicamente.

    Args:
        module_name (str): Nombre del archivo (sin .py).
        class_name (str): Nombre de la clase a instanciar.
        payload (dict): Diccionario con "function_name" y "args".

    Returns:
        Resultado de la función ejecutada.
    """
    # Importar dinámicamente el módulo
    module = importlib.import_module(module_name)

    # Verificar que la clase existe en el módulo
    if not hasattr(module, class_name):
        raise ValueError(f"La clase '{class_name}' no existe en '{module_name}'.")

    # Instanciar la clase
    class_ref = getattr(module, class_name)
    instance = class_ref()

    # Extraer el nombre de la función y sus argumentos
    function_name = payload["function_name"]
    function_args = payload.get("args", {})

    # Verificar que la función existe en la clase
    if not hasattr(instance, function_name):
        raise ValueError(f"La función '{function_name}' no existe en la clase '{class_name}'.")

    # Obtener la función
    func = getattr(instance, function_name)

    # Ejecutar la función con argumentos filtrados
    import inspect
    parametros_validos = inspect.signature(func).parameters
    args_filtrados = {k: v for k, v in function_args.items() if k in parametros_validos}

    # Llamar a la función
    return func(**args_filtrados)


# Ejemplo de uso

if __name__ == "__main__":
    payload = {
    "function_name": "create_project",
    "args": {"key": "DEATHJOHN", "project_name": "Garfield"}
    }

    resultado = ejecutar_funcion_de_objeto("wrapper", "JiraWrapper", payload)
    print(resultado)
