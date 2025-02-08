from flask_restx import Namespace


class ChatDto:
    api = Namespace('chat', description='Chat related operations')
