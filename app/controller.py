# app/controller.py

from app.model import SpeechModel, AIModelConfiguration
from app.observer import Subject

class ChatController:
    def __init__(self):
        self.speech_model = SpeechModel()
        self.ai_model_config = AIModelConfiguration()
        self.subject = Subject()

    def handle_user_input(self, user_input):
        response = self.ai_model_config.generate_response(user_input)
        self.ai_model_config.text_to_speech(response)
        return response
