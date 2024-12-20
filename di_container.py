import openai
from injector import Binder
from jira import JIRA

from config import Config
from services.audio_service import AudioService
from services.elevenlabs_service import ElevenLabsService
from services.openai_service import OpenAIService
from services.script_executor import ScriptExecutor


def configure(binder: Binder):
    # Configuración de OpenAI
    openai.api_key = Config.OPENAI_API_KEY
    openai_client = openai

    # Crear instancias de servicios
    ## Configuración de Jira
    jira_client = JIRA(server=f"https://{Config.DOMAIN}.atlassian.net",
        basic_auth=(Config.ATLASSIAN_USERNAME, Config.ATLASSIAN_API_KEY))

    openai_service = OpenAIService(openai_client=openai_client, model_type="gpt-4o-mini")
    executor = ScriptExecutor(openai_service=openai_service, jira_client=jira_client)
    elevenlabs_service = ElevenLabsService(Config.ELEVENLABS_API_KEY)
    audio_service = AudioService()
    # Registrar dependencias
    binder.bind(JIRA, to=jira_client)
    binder.bind(OpenAIService, to=openai_service)
    binder.bind(ScriptExecutor, to=executor)
    binder.bind(ElevenLabsService, to=elevenlabs_service)
    binder.bind(AudioService, to=audio_service)
