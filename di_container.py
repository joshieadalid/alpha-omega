import openai
from injector import Binder, singleton
from jira import JIRA

from config import Config
from chatbot.services.audio_service import AudioService
from chatbot.services.elevenlabs_service import ElevenLabsService
from chatbot.services.openai_service import OpenAIService
from chatbot.services.script_executor import ScriptExecutor
from authentication.repositories.user_repository import UserRepository
from authentication.services.user_service import UserService

def configure(binder: Binder):
    try:
        openai.api_key = Config.OPENAI_API_KEY
        openai_client = openai
        print("OpenAI configurado correctamente.")

        jira_client = JIRA(server=f"https://{Config.DOMAIN}.atlassian.net",
                           basic_auth=(Config.ATLASSIAN_USERNAME, Config.ATLASSIAN_API_KEY))
        print("JIRA configurado correctamente.")

        # Crear instancias de servicios
        openai_service: OpenAIService = OpenAIService(openai_client=openai_client, model_type="gpt-4o-mini")
        # executor: ScriptExecutor = ScriptExecutor(openai_service, jira_client=jira_client)
        elevenlabs_service: ElevenLabsService = ElevenLabsService(Config.ELEVENLABS_API_KEY)
        audio_service: AudioService = AudioService()


        # Registrar dependencias
        binder.bind(JIRA, to=jira_client)
        binder.bind(OpenAIService, to=openai_service)
        binder.bind(ScriptExecutor,
                    to=lambda: ScriptExecutor(binder.injector.get(OpenAIService), jira_client=jira_client),
                    scope=singleton)
        binder.bind(ElevenLabsService, to=elevenlabs_service)
        binder.bind(AudioService, to=audio_service)

        # Registrar UserRepository y UserService
        user_repository = UserRepository()
        binder.bind(UserRepository, to=user_repository, scope=singleton)
        binder.bind(UserService, to=lambda: UserService(user_repository), scope=singleton)

        print("Todas las dependencias registradas correctamente.")
    except Exception as e:
        print(f"Error en la configuración de dependencias: {e}")
        raise
