from voice_chat_robot.server.app import app
from voice_chat_robot import config
if __name__ == "__main__":
    # app.static_folder = config.STATIC_FOLDER
	app.run(
        host=config.LISTEN_IP,
        port=config.LISTEN_PORT
        )