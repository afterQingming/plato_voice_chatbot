import json
import requests
from commons import *

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
        with open('response.mp3','rb') as f:
            data = f.read()
    
    
    res=requests.post(url,data=data,headers=headers)
    js = res.json()
    if js['err_no'] == 0:
        return js['result']
    else:
        return js['err_msg']

# def vop_raw(access_token):
if __name__ == '__main__':
    t=vop_raw(access_token)
    print(t)