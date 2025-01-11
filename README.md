ESTRUCTURA DE LOS DIRECTORIOS DEL SISTEMA:

- services es para las funcionalidades, 
- controllers es para los endpoints, 
- app es para unir todo.
- static es para recursos estáticos como css y js
- templates es para las páginas html


# API Flask con Chatbot y Jira Integration

Esta API permite interactuar con un chatbot que utiliza OpenAI, soporta mensajes de texto y audio, y está integrado con Jira para realizar acciones automatizadas.

---

## **Requisitos Previos**

1. **Instalar dependencias:**
   - Python 3.x
   - Flask
   - dotenv
   - requests
   - Cualquier otra librería necesaria listada en `requirements.txt`.

2. **Variables de entorno:**
   - `ATLASSIAN_USERNAME`: Nombre de usuario de Atlassian.
   - `ATLASSIAN_API_KEY`: Clave de API de Atlassian.

3. **Archivos requeridos:**
   - `services/openai_service.py`: Implementación del chatbot utilizando OpenAI.
   - `services/jira_service.py`: Funciones para integrar Jira.
   - `services/project_manager.py`: Lógica para la administración de proyectos.

---

## **Rutas Disponibles**

### **Frontend**
- `GET /`  
  Muestra la página principal.

- `GET /main`  
  Muestra la página principal de la aplicación.

- `GET /login`  
  Muestra la página de inicio de sesión.

- `GET /register`  
  Muestra el formulario de registro.

- `POST /register`  
  Registra al usuario y redirige a la página de inicio de sesión.

---

### **Chatbot**

#### **Interactuar con el chatbot**
- `POST /chatbot`  
  Recibe un mensaje en formato JSON o un archivo de audio para procesarlo.  
  **Parámetros:**
  - **JSON:** `{"message": "texto del mensaje"}`
  - **Audio:** Archivo de audio en el campo `audio`.  
  **Respuesta:**  
  ```json
  {
    "reply": "Respuesta generada por el chatbot"
  }
  ```

#### **Mensajes de texto**
- `POST /chatbot/text`  
  Similar a `/chatbot`, pero solo acepta mensajes de texto.  
  **Parámetros:**  
  ```json
  {"message": "texto del mensaje"}
  ```

#### **Mensajes de audio**
- `POST /chatbot/audio`  
  Acepta solo archivos de audio para procesar.  
  **Respuesta:**  
  ```json
  {
    "reply": "Respuesta generada por el chatbot"
  }
  ```

---

### **Jira Integration**

#### **Acciones en Jira**
Las siguientes acciones se ejecutan en función de `action_code` enviado al chatbot:

| Código | Acción                     | Descripción                                         |
|--------|----------------------------|-----------------------------------------------------|
| `1`    | Crear proyecto             | Crea un nuevo proyecto en Jira.                     |
| `2`    | Eliminar proyecto          | Elimina un proyecto existente basado en un mensaje. |
| `3`    | Listar proyectos recientes | Obtiene una lista de proyectos recientes.           |
| `4`    | Listar usuarios recientes  | Obtiene una lista de usuarios recientes.            |

---

## **Instrucciones para Correr el Proyecto**

1. **Cargar variables de entorno:**
   ```bash
   export ATLASSIAN_USERNAME="tu_usuario"
   export ATLASSIAN_API_KEY="tu_clave_api"
   ```

2. **Ejecutar la aplicación:**
   ```bash
   python main.py
   ```

3. **Acceder en el navegador:**
   - URL local: `http://localhost:8080`

---

## **Estructura del Proyecto**

```
├── controllers/
│   └── chatbot_controller.py
├── services/
│   ├── jira_service.py
│   ├── openai_service.py
│   └── project_manager.py
├── templates/
│   ├── index.html
│   ├── login.html
│   ├── main.html
│   └── register.html
├── main.py
├── README.md
└── .env
```

---

## **Errores Comunes**

- `400 Bad Request`: Parámetros faltantes o inválidos.
- `500 Internal Server Error`: Error inesperado en el servidor.
- `Error en Jira`: Problemas al ejecutar una acción en Jira.

---

## **Contribuciones**

Este proyecto es para uso personal, pero se puede ampliar fácilmente. Cualquier mejora o sugerencia es bienvenida.

### Instrucciones para desplegar el servidor

#### **Frontend (React)**
1. Abre una terminal y navega al directorio `frontend/`:
   ```bash
   cd frontend/
   ```
2. Instala las dependencias:
   ```bash
   npm install
   ```
3. Genera la versión optimizada del proyecto:
   ```bash
   npm run build
   ```
4. Para servir la aplicación en el puerto 3000, puedes usar cualquiera de estas dos opciones:
   - Opción 1 (con `serve`):
     ```bash
     npx serve -s build -l 3000
     ```
   - Opción 2 (con `npm`):
     ```bash
     npm run serve
     ```

#### **Backend (Flask)**
1. Navega al directorio del backend en la terminal.
2. Instala las dependencias necesarias desde `requirements.txt`:
   ```bash
   pip install -r requirements.txt
   ```
3. Ejecuta la aplicación Flask en el puerto 5000:
   ```bash
   flask run --host=0.0.0.0 --port=5000
   ```

#### **Problemas comunes**
- Si la página muestra un error de conexión al servidor, verifica si la base de datos está funcionando correctamente.
- Para reiniciar la base de datos, ejecuta el script `reset_database.py`:
   ```bash
   python reset_database.py
   ```
