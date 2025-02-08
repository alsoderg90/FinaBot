from google import genai
import uuid
from ..config import Config


class ChatService:
    def __init__(self):
        self.__client = genai.Client(api_key=Config.GEMINI_API_KEY)

    def get_answer(self, user_input):
        client = self.__get_client()
        response = client.models.generate_content(
            model="gemini-2.0-flash", contents=user_input['data']['input']
        )
        uuid1 = uuid.uuid1()
        return {
            "content": response.text,
            "id": uuid1,
            "role": "ai"
        }

    def __get_client(self):
        return self.__client


