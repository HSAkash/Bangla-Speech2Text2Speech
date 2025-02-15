from gtts import gTTS
from bnsttts import logger

class TTS:
    """ Text to speech conversion"""

    def __init__(self):
        pass

    def speak(self, text: str, save_path:str, lang: str = "bn", slow: bool=False) -> None:
        """Speaks given text in given language

        Args:
            text (str): Text to be spoken
            save_path (str): Path to save the audio file
            lang (str, optional): Language code. Defaults to "en".
            slow (bool, optional): Speak slowly. Defaults to False.
        """
        tts = gTTS(text=text, lang=lang, slow=slow)
        tts.save(save_path)


if __name__ == "__main__":
    tts = TTS()

    logger.info("Converting text to speech")
    tts.speak("আমি বাংলায় কথা বলতে পারি", "data/tts/output.mp3", lang="bn")
    logger.info("Text to speech conversion completed")