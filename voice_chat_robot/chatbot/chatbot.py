from chatterbot import ChatBot
# from chatterbot.trainers import ListTrainer
# from chatterbot.trainers import ChatterBotCorpusTrainer

# Creating ChatBot Instance
#chatbot = ChatBot('CoronaBot')
chatbot = ChatBot(
    'PlatoBot',
    # storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        # 'chatterbot.logic.MathematicalEvaluation',
        # 'chatterbot.logic.TimeLogicAdapter',
        # 'chatterbot.logic.BestMatch',
        # {
        #     'import_path': 'chatterbot.logic.BestMatch',
        #     'default_response': 'I am sorry, but I do not understand. I am still learning.',
        #     'maximum_similarity_threshold': 0.90
        # },
        'adapters.platobot.PlatoLogicAdapter'
    ],
    # database_uri='sqlite:///database.sqlite3'
)
