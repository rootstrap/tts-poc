import io

from elevenlabs.client import ElevenLabs


def get_elevenlabs_client(api_key: str) -> ElevenLabs:
    """
    Create and return an ElevenLabs client using the provided API key.

    Args:
        api_key (str): The ElevenLabs API key.

    Returns:
        ElevenLabs: An instance of the ElevenLabs client.
    """
    return ElevenLabs(api_key=api_key)


def get_elevenlabs_tts(client: ElevenLabs, voice: str, text: str) -> str:
    """
    Get a text-to-speech response from the ElevenLabs client.

    Args:
        client (ElevenLabs): The ElevenLabs client instance.
        voice (str): The voice to use for generating the speech.
        text (str): The text to convert to speech.

    Returns:
        str: The URL of the generated audio file.
    """
    tts_response = client.text_to_speech.convert(
        text=text,
        voice_id=voice,
        #  language_code=lang,
    )
    return io.BytesIO(b"".join(tts_response))
