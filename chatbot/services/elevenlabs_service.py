from enum import Enum
from typing import Tuple, IO
from elevenlabs import VoiceSettings
from elevenlabs.client import ElevenLabs
from io import BytesIO

class VoiceOption(Enum):
    WOMAN = "wJqPPQ618aTW29mptyoc"  # Mujer
    MAN = "JBFqnCBsd6RMkjVDRZzb"    # Hombre
    IDALIA = "SvU0B5XIX9vlVyFfY2Kc"  # Idalia


class ElevenLabsService:
    def __init__(self, api_key: str):
        self.client = ElevenLabs(api_key=api_key)

    def tts_stream(self, text: str, voice: VoiceOption=VoiceOption.IDALIA) -> Tuple[IO[bytes], str, dict]:
        """
        Convierte texto a audio y devuelve un flujo de bytes con su mimetype y headers.
        """
        response = self.client.text_to_speech.convert(
            voice_id=voice,
            optimize_streaming_latency="0",
            output_format="mp3_22050_32",
            text=text,
            model_id="eleven_multilingual_v2",
            voice_settings=VoiceSettings(
                stability=0.0,
                similarity_boost=1.0,
                style=0.0,
                use_speaker_boost=True,
            ),
        )

        audio_stream = BytesIO()
        for chunk in response:
            if chunk:
                audio_stream.write(chunk)

        audio_stream.seek(0)
        mimetype = "audio/mpeg"
        headers = {"Content-Disposition": "attachment; filename=output_audio.mp3"}
        return audio_stream, mimetype, headers

    def tts_to_mp3(self, text: str) -> Tuple[IO[bytes], str, dict]:
        """
        Convierte texto a audio y devuelve un flujo de bytes junto con mimetype y headers.
        """
        return self.tts_stream(text)
