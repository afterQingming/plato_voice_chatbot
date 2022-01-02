# from chatbot import chatbot
from flask import Flask, render_template, request, jsonify,send_file,make_response,stream_with_context
from requests.models import Response
import voiceutils as vutils 
# import chatbot
import chat_bot
import json
app = Flask(__name__)
app.static_folder = 'static'
bot = chat_bot.PlatoChatBotAPI()
app.config['JSON_AS_ASCII'] = False
@app.route("/")
def home():
    context={
            'static_local':'static',
            'static_global':'static',
            'get_bot_response': "get_bot_response",
            'get_voice_response': "get_voice_response",
            'text2voice': "text2voice",
        }
    return render_template("index.html",**context)

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    re=bot.get_response(userText)
    return " ".join(re)
    # return str(chatbot.get_response(userText))


@app.route("/get_voice", methods=['GET', 'POST'])
def get_voice_response():
    if request.method == 'POST':
        file = request.files['audio_file']
        if file:
            # print(file)
            # print('file.name:', file.name)
            # print('file.filename:', file.filename)
            # print(dir(file))
            # print(file.headers)
            r = vutils.vop_raw(vutils.access_token,file)
            r= ' '.join(r)
            # print(r)
            # filename = secure_filename(file.filename)
            # filename = os.path.join(app.config['UPLOAD_FOLDER'], filename + ".pcm")
            # file.save(filename)
            # result = get_speech_result(filename)
            # os.remove(filename)
            # print(result)
            # if 'result' in result and len(result['result']):
            #     return result['result'][0]
            # return redirect(url_for('upload', filename=filename))
            re=bot.get_response(r)
            reponse = {
                'user': r,
                "bot": " ".join(re)
            }
            return jsonify(reponse)
    
    return " "

    
# @app.route("/voice2text")
# def voice2text():
#     userText = request.post.get('msg')
    
#     if request.method == 'POST':
#         request.get_data()
#         raw = vutils.get_voice(userText,vutils.access_token)
#         return  Response(send_file(raw, "audio/mpeg3"))

    
@app.route("/text2voice", methods=['GET','POST'])
def text2voice():
    print(request.args)
    userText = request.args.get('msg')
    # userText=request.get_data()
    # re=bot.get_response(userText)
    print(userText)
    raw = vutils.get_voice(text=userText,access_token=vutils.access_token)
    # @stream_with_context
    # def generate():
    #     path = 'response'
    #     with open(path, 'rb') as fmp3:
    #         data = fmp3.read(1024)
    #         while data:
    #             yield data
    #             data = fmp3.read(1024)
    # return Response(generate())
    f=open("response.wav",'rb')
    return  send_file(f, "audio/wav")
    # return  Response(raw, mimetype="audio/mpeg3")

if __name__ == "__main__":
	app.run(host='0.0.0.0',port=4999)