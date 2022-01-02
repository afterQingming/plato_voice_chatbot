import json
import requests
from . import config
CUID=config.CUID
appKey =config.appKey
appSecret =config.appSecret
access_token = config.access_token

TOK_URL = "https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id={}&client_secret={}"

TTS_URL = "https://tsn.baidu.com/text2audio"
VOP_URL = "http://vop.baidu.com/server_api"

def get_token():
    url=TOK_URL.format(appKey, appSecret)
    re=requests.get(url)
    return re.json["access_token"]

def get_voice(text, access_token):
    data = {
        'tex': text,
        'tok': access_token,
        'cuid': CUID,
        'ctp': 1,
        'lan': "zh",
        'aue': 6
    }
    res=requests.post(TTS_URL,data=data)#data可以直接传字典
    the_hearders=res.headers
    print(the_hearders)
    if the_hearders['Content-Type'] =="aplication/json":
        print(the_hearders)
        print(res.content)
        # return res.content
    else:
        with open('response.wav','wb') as fw:#把二进制文件下载下来，写入到'魔鬼中的天使.mp3'
            fw.write(res.content)
    return ""

def add_url_param(base_url, param_dict):
    t = "?"
    for key in param_dict:
        t = t+"&{}={}".format(key, param_dict[key])
    return base_url + t

def vop_raw(access_token, data=None):
    url = add_url_param(VOP_URL,  {
        'cuid': CUID,
        'token':access_token,
    })
    headers = {
        'Content-Type' :'audio/pcm;rate=16000',
    }
    # param_hearder = json.dumps(headers)
    if data is None:
        with open('魔鬼中的天使.mp3','rb') as f:
            data = f.read()
    
    
    res=requests.post(url,data=data,headers=headers)
    js = res.json()
    if js['err_no'] == 0:
        return js['result']
    else:
        return js['err_msg']