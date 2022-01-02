
import requests
import json
from .. import voice_utils as vutils
from .. import config 
class WebPlatoChatBotAPI:

    @classmethod
    def get_response(self, text=""):
        texts = [text]
        data = {"data": texts}
        # 发送post请求，content-type类型应指定json方式，url中的ip地址需改为对应机器的ip
        url = config.plato_url
        # 指定post请求的headers为application/json方式
        headers = {"Content-Type": "application/json"}

        r = requests.post(url=url, headers=headers, data=json.dumps(data))
        return r.json()['results']