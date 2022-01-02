# _*_ coding: utf-8 _*_
DEBUG = True
LISTEN_IP = '0.0.0.0'
LISTEN_PORT = '4999'
STATIC_FOLDER = "static"

# 路由配置
ROUTER_CHATBOT = "/chatbot"

# 语音API设置

CUID="DAFDAFAFAFA"
appKey =""
appSecret =""
access_token = ""

# plato开放的路径
plato_url =  "http://localhost:8866/predict/plato-mini"
# plato_url =  "http://172.18.167.33:8866/predict/plato-mini"

# UPLOAD_FOLDER = 'upload'
# from flask_uploads import UploadSet, configure_uploads, IMAGES, patch_request_class
# UPLOADED_PHOTOS_DEST = './images/'  # 相对路径下的文件夹images
# UPLOADED_PHOTO_ALLOW = IMAGES		# 限制只能够上传图片
# UPLOADS_DEFAULT_URL = 'http://127.0.0.1:9000/'