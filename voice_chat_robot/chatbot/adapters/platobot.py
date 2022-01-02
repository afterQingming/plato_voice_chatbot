from chatterbot.logic import LogicAdapter
from ..simple_plato_api import WebPlatoChatBotAPI




class PlatoLogicAdapter(LogicAdapter):
    def __init__(self, chatbot, **kwargs):
        super().__init__(chatbot, **kwargs)

    def can_process(self, statement):
        return True

    def process(self, input_statement, additional_response_selection_parameters):
        import random

        # Randomly select a confidence between 0 and 1
        confidence = random.uniform(0, 1)

        text = WebPlatoChatBotAPI.get_response(input_statement.text)
        selected_statement = input_statement
        input_statement.text = text
        selected_statement.confidence = confidence

        return selected_statement

if __name__ =="__main__":
    t=PlatoChatBotAPI()
    h=t.get_response("你好")
    print(h)