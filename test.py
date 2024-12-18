import services.jira_service as jir

if __name__ == "__main__":
    actions = [
        {"function_name": "projects", "args": {}},
        {"function_name": "create_project", "args": {"key": "IGN", "name": "Iguana"}}
    ]
    resultados = jir.process_actions(actions)
    print(resultados)