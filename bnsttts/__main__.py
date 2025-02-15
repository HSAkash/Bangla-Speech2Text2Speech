import os
import click
from bnsttts.stt import STT
from bnsttts.tts import TTS
from bnsttts import logger


# Click settings
CONTEXT_SETTINGS = {"help_option_names": ["-h", "--help"]}


@click.command(context_settings=CONTEXT_SETTINGS)
@click.argument('content', required=True)
@click.option('--output', '-o', type=str, default='output.mp3', help='Where text to audio file will be stored.')
@click.option(
    '--lang', '-l', 
    type=str,
    default='bn', 
    help='Language to speak in (e.g., en, bn')

@click.option('--tts', '-t', is_flag=True, help='For text to speech.')
@click.option('--stt', '-s', is_flag=True, help='For speech to text.')
@click.option('--slow', is_flag=True, help='For slow speech.')

def main(content, output, lang, tts, stt, slow) -> str:
    """
    A CLI tool to convert text to speech or speech to text.

    Args:
        content (str): audio file path or text
        output (str): Where text to audio file will be stored.
        lang (str): Language to speak in (e.g., en, bn)
        tts (bool): For text to speech.
        stt (bool): For speech to text.
        slow (bool): For slow speech.

    Returns:
        str: Path to the generated audio file or transcribe text.
    """
    if tts:
        print(output)
        if not os.path.exists(os.path.dirname(output)):
            logger.info(f"Creating directory {os.path.dirname(output)}")
        tts = TTS()
        audio_file_path = tts.speak(content, output, lang=lang, slow=slow)
        logger.info(f"Audio file saved at {audio_file_path}")
        
    elif stt:
        if not os.path.exists(content):
            logger.error(f"Audio file not found at {content}")
            return
        # Convert audio file to text
        stt = STT()
        transcriptions = stt.transcribe(content)
        logger.info(f"Transcribed text: {transcriptions[0]}")

if __name__ == "__main__":
    # Ensure Click executes the `main()` function with the CLI arguments
    response = main()