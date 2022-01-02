import json
import requests

CUID="DAFDAFAFAFA"
appKey ="EACChjYLG7LQBzVPUD1lwBAG"
appSecret ="wSTyOPwhqKEonYlkW53HE7bIRwfGHjm4"
access_token = "24.bdb23ceeedefc1e9173204cc1babc922.2592000.1642491688.282335-25374783"

TOK_URL = "https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id={}&client_secret={}"

TTS_URL = "https://tsn.baidu.com/text2audio"
VOP_URL = "http://vop.baidu.com/server_api"

def get_token():
    url=TOK_URL.format(appKey, appSecret)
    re=requests.get(url)
    return re.json["access_token"]