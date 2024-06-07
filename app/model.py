# app/model.py

import os
from google.cloud import speech
import sounddevice as sd  # Import sounddevice instead of pyaudio
import genai  # Make sure this is the correct import for the GenerativeModel class
from gtts import gTTS
import playsound

class SpeechModel:
    def __init__(self):
        # Set the path to your Google Cloud service account JSON file
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/Users/adrocx/Downloads/western-net-422115-984ccca6d814.json"
        self.speech_client = speech.SpeechClient()

    def get_audio_input(self):
        # Implementation for getting audio input
        pass

    def transcribe_audio(self, audio_data):
        # Implementation for transcribing audio
        pass

class AIModelConfiguration:
    def __init__(self):
        self.model = genai.GenerativeModel()  # No arguments here

    def generate_response(self, input_text):
        response = self.model.generate(input_text)
        return response

    def text_to_speech(self, text):
        tts = gTTS(text=text, lang='en')
        tts.save("response.mp3")
        playsound.playsound("response.mp3")
