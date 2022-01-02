from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for,
    jsonify,send_file,make_response,stream_with_context
)
from requests.models import Response
from werkzeug.exceptions import abort

# from flaskr.auth import login_required
# from flaskr.db import get_db
from ... import voice_utils as vutils
# import chatbot
from . import application_api 
import json

bp = Blueprint(
    'chatbot', 
    __name__,
    template_folder='templates',
    static_folder='static',
    # static_url_path = 'chatbot/static'
)

bot = application_api.PlatoChatBotAPI()
@bp.route("/")
def home():
    context={
            'static_local':'chatbot.static',
            'static_global':'static',
            'get_bot_response': "chatbot.get_bot_response",
            'get_voice_response': "chatbot.get_voice_response",
            'text2voice': "chatbot.text2voice",
        }
    return render_template("index.html",**context)

@bp.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    re=bot.get_response(userText)
    return " ".join(re)
    # return str(chatbot.get_response(userText))


@bp.route("/get_voice", methods=['GET', 'POST'])
def get_voice_response():
    if request.method == 'POST':
        file = request.files['audio_file']
        if file:
            user_text, bot_text= bot.get_voice_response(file)
            reponse = {
                'user': user_text,
                "bot": bot_text
            }
            return jsonify(reponse)
        else:
            return jsonify(
                {
                    'user': "",
                    "bot": "不好意思服务异常，不能听到您的声音"
                }
            )
    
    return " "

    
    
@bp.route("/text2voice", methods=['GET','POST'])
def text2voice():
    print(request.args)
    userText = request.args.get('msg')
    print(userText)
    raw = vutils.get_voice(text=userText,access_token=vutils.access_token)
    f=open("response.wav",'rb')
    return  send_file(f, "audio/wav")
