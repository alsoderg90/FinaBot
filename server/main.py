from flask import Flask, request, jsonify, make_response
from flask_cors import CORS
from google import genai
import requests
from environs import Env
import uuid

app = Flask(__name__)
CORS(app)

env = Env()
env.read_env()

app.config['GEMINI_APIKEY'] = env.str('GEMINI_APIKEY')
GEMINI_API_URL = "https://api.gemini.openai.com/v1/chat"


@app.route("/")
def getroot():
    return "Welcome!"


@app.route("/chat", methods=['POST'])
def chat():
    try:
        client = genai.Client(api_key=app.config['GEMINI_APIKEY'])
        user_input = request.get_json()
        response = client.models.generate_content(
            model="gemini-2.0-flash", contents=user_input['data']['input']
        )
        uuid1 = uuid.uuid1()
        answer = {
            "content": response.text,
            "id": uuid1,
            "role": "ai"
        }
        return make_response(jsonify(answer), 201)

    except Exception as e:
        print("exception")
        print(e)
        return make_response(jsonify({"error": str(e)}), 500)


if __name__ == "__main__":
    app.run(debug=True)
