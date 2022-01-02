# 部署
	先获取百度语音识别及合成API
	修改 appKey，appSecret，access_token
	access_token获取后可以保证一个月

	最好预先下载plato模型参数

- 在plato文件夹内

	hub serving start --config config.json
- 在顶目录下
	
	python main.py


## ai技术支持
### 语音识别+语音合成 API
	文档：https://ai.baidu.com/ai-doc/index/SPEECH
### 闲聊机器人：本地服务器部署 plato-mini
	paddlehub plato-mini
	paddlehub serving
		文档1：https://github.com/PaddlePaddle/PaddleHub/blob/release/v2.1/docs/docs_ch/tutorial/serving.md
		文档2：https://www.paddlepaddle.org.cn/hubdetail?name=plato-mini&en_category=TextGeneration
		命令1：hub serving start --config config.json
		命令2：hub serving start -m plato-mini

## 软件支持：
- 前端：

	recorder:https://github.com/2fps/recorder.git
	界面：https://github.com/AnTi-anti/chat_bot.git
- 后端：

	flask+ paddlehub serving

- 后续：

	后端添加chatterbot作为核心
	使用自定义logic adapter 插入plato
	https://chatterbot.readthedocs.io/en/stable/logic/create-a-logic-adapter.html