from flask import request, jsonify, make_response
from flask_restx  import Resource
from ..utils.dto import ChatDto
from ..services.chat_service import ChatService
from ..services.document_search_service import DocumentSearchService
import requests

api = ChatDto.api
chat_service = ChatService()
document_search_service = DocumentSearchService()

@api.route("/", methods=['POST'], strict_slashes=False)
class Chat(Resource):
    def post(self):
        try:
            user_request = request.get_json()
            user_input = user_request['data']['input']
            if (user_input is None) or (user_input == ""):
                return make_response(jsonify({"error": "Input is required.", "error_code": 400}), 400)
            relevant_document = document_search_service.search_relevant_document(user_input, vector_type='tfidf')
            answer = chat_service.get_answer(user_input, relevant_document)
            return make_response(jsonify(answer), 201)

        except Exception as e:
            print("exception")
            print(e)
            return make_response(jsonify({"error": str(e), "error_code": 500}), 500)


