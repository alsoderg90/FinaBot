from flask import request, jsonify, make_response
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restx  import Resource
from ..utils.dto import ChatDto
from ..services.chat_service import ChatService
from ..services.document_search_service import DocumentSearchService
from ..services.query_transformation_service import QueryTransformationService
import traceback
import requests

api = ChatDto.api
chat_service = ChatService()
document_search_service = DocumentSearchService()
query_transformation_service = QueryTransformationService()


@api.route("/", methods=['POST'], strict_slashes=False)
class Chat(Resource):
    @staticmethod
    def post():
        try:
            user_request = request.get_json()
            user_input = user_request['data']
            conversation_history = user_request['history']
            if (user_input is None) or (user_input == ""):
                return make_response(jsonify({"error": "Input is required.", "error_code": 400}), 400)
            if len(conversation_history) > 0:
                rephrased_query = query_transformation_service.rephrase_query(conversation_history, user_input)
                new_user_input = chat_service.get_answer(rephrased_query)
                user_input = new_user_input['content'] if new_user_input else user_input
            print(user_input)
            relevant_documents = document_search_service.search_relevant_documents(user_input, vector_type='tfidf')
            query = query_transformation_service.default_query(relevant_documents, user_input)
            answer = chat_service.get_answer(query)
            return make_response(jsonify(answer), 201)

        except Exception as e:
            print("exception")
            print(e)
            print(traceback.format_exc())
            return make_response(jsonify({"error": str(e), "error_code": 500}), 500)


