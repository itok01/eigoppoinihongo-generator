from jaconv import h2z
import pykakasi
from google.cloud import texttospeech


def genEnSpeech(text):
    kakasi = pykakasi.kakasi()

    kakasi.setMode("H", "a")
    kakasi.setMode("K", "a")
    kakasi.setMode("J", "a")
    kakasi.setMode("r", "Hepburn")

    conv = kakasi.getConverter()

    t2s_client = texttospeech.TextToSpeechClient()

    synthesis_input = texttospeech.types.SynthesisInput(
        text=conv.do(h2z(text)))

    voice = texttospeech.types.VoiceSelectionParams(
        language_code='en-US',
        ssml_gender=texttospeech.enums.SsmlVoiceGender.NEUTRAL)

    audio_config = texttospeech.types.AudioConfig(
        audio_encoding=texttospeech.enums.AudioEncoding.MP3)

    response = t2s_client.synthesize_speech(
        synthesis_input, voice, audio_config)

    return response.audio_content
