import types

from google.cloud import speech

from nextpy.ai.models.audio.speech_to_text.base import SpeechToText
from nextpy.utils.logger import get_logger
from nextpy.utils.singleton import Singleton

logger = get_logger(__name__)
config = types.SimpleNamespace(
    **{
        "web": {
            "encoding": speech.RecognitionConfig.AudioEncoding.WEBM_OPUS,
            "sample_rate_hertz": 48000,
            "language_code": "en-US",
            "max_alternatives": 1,
        },
        "terminal": {
            "encoding": speech.RecognitionConfig.AudioEncoding.LINEAR16,
            "sample_rate_hertz": 44100,
            "language_code": "en-US",
            "max_alternatives": 1,
        },
    }
)


class Google(Singleton, SpeechToText):
    def __init__(self):
        super().__init__()
        logger.info("Setting up [Google Speech to Text]...")
        self.client = speech.SpeechClient()

    def transcribe(self, audio_bytes, platform, prompt="", language="en-US") -> str:
        batch_config = speech.RecognitionConfig(
            {
                "speech_contexts": [speech.SpeechContext(phrases=prompt.split(","))],
                **config.__dict__[platform],
            }
        )
        batch_config.language_code = language
        if language != "en-US":
            batch_config.alternative_language_codes = ["en-US"]
        response = self.client.recognize(
            config=batch_config, audio=speech.RecognitionAudio(content=audio_bytes)
        )
        if not response.results:
            return ""
        result = response.results[0]
        if not result.alternatives:
            return ""
        return result.alternatives[0].transcript
