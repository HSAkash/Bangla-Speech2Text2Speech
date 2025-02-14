import nemo.collections.asr as nemo_asr
from bnsttts.utils import get_config
from typing import List
from bnsttts import logger
import librosa

class STT:
    """Speech to Text class using Nemo ASR model"""
    def __init__(self, ):
        self.config = get_config()
        self.model = nemo_asr.models.ASRModel.from_pretrained(
            model_name = self.config.stt.model_name
        )

    def preprocess(self, audio_file_path: str) -> str:
        """Preprocesses audio file

        Args:
            audio_file_path (str): Path to the audio file

        Returns:
        str: Path to the preprocessed audio file
        """
        y, sr = librosa.load(audio_file_path)
        # Convert stereo audio to mono by averaging channels if necessary
        if y.ndim == 2:
            y = librosa.to_mono(y)
        return y

    def transcribe(self, audio_file_path: str) -> List[str]:
        """Transcribes audio file to text

        Args:
            audio_file_path (str): Path to the audio file

        Returns:
        List[str]: List of transcribed bangla text
        """
        # Convert stereo audio to mono by averaging channels if necessary
        y = self.preprocess(audio_file_path)
        transcription = self.model.transcribe([y])
        return transcription

if __name__ == "__main__":
    stt = STT()
    transcriptions = stt.transcribe("data/stt/01.wav")
    for transcription in transcriptions:
        logger.info(transcription)