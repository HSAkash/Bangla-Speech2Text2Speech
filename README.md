# **Bangla Speech-to-Text & Text-to-Speech** 🎙️🔊  

This project enables **Bangla Speech-to-Text (STT) and Text-to-Speech (TTS)** conversion. It utilizes advanced AI models to achieve accurate transcription and natural-sounding speech synthesis.  

✨ **Technologies Used:**  
- 🗣️ **Speech-to-Text (STT):** [hishab/titu_stt_bn_fastconformer](https://huggingface.co/hishab/titu_stt_bn_fastconformer) – A powerful ASR model optimized for Bangla.  
- 🔊 **Text-to-Speech (TTS):** [gTTS](https://github.com/pndurette/gTTS) – A Google Text-to-Speech library for generating natural Bangla speech.  



## Setup
```
pip install -q git+https://github.com/HSAkash/Bangla-Speech2Text2Speech.git
```
or
```
pip install bnsttts
```

## How to use in code
### Speech to text
```
from bnsttts.stt import STT
stt = STT()
response = stt.transcribe("data/stt/01.wav")
print(response[0])
```
### Text to speech
```
from bnsttts.tts import TTS
tts = TTS()
tts.speak("আমি বাংলায় কথা বলতে পারি", "data/tts/output.mp3", lang="bn")
```



## Run commands
### Speech to text
```
bnsttts -s <audio_file_path>
```
#### Example
🎵 Listen to the sample audio: [Click here](data/stt/01.wav)

```
bnsttts --stt data/stt/01.wav
```
##### output:
```
শুন কে আমি শিশু সুলভ বোক আমি মিশ্রণ হিসেবে বর্ণ না করব তিনি প্রায়ই সময় ডিমেরে এক হাজার ডলার খরচ করতেন তিনি তার বন্ধুদের সামনে সম্পথের শো অফ করতেন তিনি প্রকাশ্যে এবং উচ্চ সরে তার সম্পদ নিয়ে বড়াই করতেন প্রায় সময় মাতাল অবস্থায় এই হোটেল থেকে বের হতেন একদিন তিনি আমার এক সহকর্মীর হাতে নগদ কয়েক হাজার ডলার দিয়ে বললেন রাস্তার পাশে গয়নার দোকানে যাও এবং আমার জন্য কয়েক ডলার মূল্যের এক হাজার একটি সোনার কয়েন কিনে আন এক ঘন্টা পর হাতে সোনার কয়েন নিয়ে প্রকৌশলী এবং তার বন্ধুরা প্রশান্ত
```
### Text to Speech
```
bnsttts -t <text>
```
#### Example
```
bnsttts --tts "আমি বাংলায় কথা বলতে পারি" -o data/tts/output.mp3
```
##### output:
🎵 Listen to the sample output: [Click here](data/tts/output.mp3)
```
Audio file saved at data/tts/output.mp3
```

### Help command
```
bnsttts -h
```
```
Usage: bnsttts [OPTIONS] CONTENT

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

Options:
  -o, --output TEXT  Where text to audio file will be stored.
  -l, --lang TEXT    Language to speak in (e.g., en, bn
  -t, --tts          For text to speech.
  -s, --stt          For speech to text.
  --slow             For slow speech.
  -h, --help         Show this message and exit.
```