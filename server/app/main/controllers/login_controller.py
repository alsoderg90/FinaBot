from google.auth.transport import requests
from google.oauth2 import id_token

from ..utils.dto import LoginDto
from ..config import Config
from flask_restx  import Resource
from flask import request, jsonify, make_response
from ..services.user_service import UserService
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity

api = LoginDto.api
user_service = UserService()

@api.route('/user', methods=['GET'])
class Auth(Resource):
    @staticmethod
    @jwt_required()
    def get():
        identity = get_jwt_identity()
        user = user_service.find_by_email(identity)
        print(identity, user)
        if not user:
            return make_response(jsonify({"error": "User not found", "error_code": 401}), 401)
        return make_response(jsonify({
            "user": user
        }), 200)


@api.route('/callback', methods=['POST'])
class Login(Resource):
    @staticmethod
    def post():
        login_request = request.get_json()
        token = login_request['data']['credential']

        if not token:
            return jsonify({"error": "Token is missing"}), 400

        try:
            id_info = id_token.verify_oauth2_token(token, requests.Request(), Config.GOOGLE_OAUTH_CLIENT_ID)

            user_info = {
                "email": id_info["email"],
                "name": id_info.get("name"),
                "picture": id_info.get("picture"),
                "user_id": id_info["sub"]
            }

            user = user_service.find_or_create_user(**user_info)
            access_token = create_access_token(identity=user["email"])
            print(access_token)

            return make_response(jsonify({
                "access_token": access_token,
                "user": user
            }), 200)


        except Exception as e:
            print("exception")
            print(e)
            return jsonify({"error": "Invalid token"}), 400
