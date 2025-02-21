from google import genai
import uuid
from ..config import Config


class ChatService:
    def __init__(self):
        self.__client = genai.Client(api_key=Config.GEMINI_API_KEY)

    def get_answer(self, query):
        return self.__generate_answer(query)


    def __generate_answer(self, query):
        client = self.__get_client()
        response = client.models.generate_content(
            model="gemini-2.0-flash", contents=query
        )
        uuid1 = uuid.uuid1()
        return {
            "content": response.text,
            "id": uuid1,
            "role": "ai"
        }

    def __get_client(self):
        return self.__client


