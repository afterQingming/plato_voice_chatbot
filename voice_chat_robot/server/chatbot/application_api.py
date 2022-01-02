# import paddlehub as hub

import requests
import json
from ... import voice_utils as vutils
from ...chatbot.simple_plato_api import WebPlatoChatBotAPI
# from ..chatbot import chatbot
class PlatoChatBotAPI:
    def __init__(self):
        self.load_model()
    
    def load_model(self):
        pass
    def get_voice_response(self, file):
        text = vutils.vop_raw(vutils.access_token,file)
        user_text = ' '.join(text)
        bot_text=self.get_response(user_text)
        return user_text, bot_text

    def get_response(self, text=""):
        responses = WebPlatoChatBotAPI.get_response(text)

        return " ".join(responses)
        
if __name__ =="__main__":
    t=PlatoChatBotAPI()
    h=t.get_response("你好")
    print(h)