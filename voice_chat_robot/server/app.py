from flask import (
    Flask,Blueprint, flash, g, redirect, render_template, request, url_for,
    jsonify,send_file,make_response,stream_with_context
)
from requests.models import Response

from . import chatbot

from .. import config

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
app.register_blueprint(chatbot.bp, url_prefix=config.ROUTER_CHATBOT)

@app.route("/")
def home():
    return redirect(url_for('chatbot.home'))
if __name__ == "__main__":
	app.run(host='0.0.0.0',port=4999)