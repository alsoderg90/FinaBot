from flask import request, jsonify, make_response
from flask_restx  import Resource
from ..utils.dto import ChatDto
from ..services.chat_service import ChatService
import requests

api = ChatDto.api
chat_service = ChatService()

@api.route("/", methods=['POST'], strict_slashes=False)
class Chat(Resource):
    def post(self):
        try:
            user_input = request.get_json()
            answer = chat_service.get_answer(user_input)
            return make_response(jsonify(answer), 201)

        except Exception as e:
            print("exception")
            print(e)
            return make_response(jsonify({"error": str(e)}), 500)


