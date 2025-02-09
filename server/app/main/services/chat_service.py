from google import genai
import uuid
from ..config import Config


class ChatService:
    def __init__(self):
        self.__client = genai.Client(api_key=Config.GEMINI_API_KEY)

    def get_answer(self, user_input, relevant_document):
        return self.__generate_answer(user_input, relevant_document)


    def __generate_answer(self, user_input, relevant_document):
        client = self.__get_client()
        template = """Answer the question based only on the following context:
        %s

        Question: %s
        """ % (relevant_document, user_input)
        response = client.models.generate_content(
            model="gemini-2.0-flash", contents=template
        )
        print(relevant_document)
        uuid1 = uuid.uuid1()
        return {
            "content": response.text,
            "id": uuid1,
            "role": "ai"
        }

    def __get_client(self):
        return self.__client


