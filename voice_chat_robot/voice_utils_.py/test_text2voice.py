import json
import requests

TTS_URL = "https://tsn.baidu.com/text2audio"
from commons import *
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

if __name__ == '__main__':
    get_voice("你好",access_token)