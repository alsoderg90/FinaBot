from flask_restx import Api
from flask import Blueprint
from .main.controllers.chat_controller import api as chat_ns

blueprint = Blueprint('api', __name__)

api = Api(
    blueprint,
    title='FLASK RESTX API BOILER-PLATE WITH JWT',
    version='1.0',
    description='A boilerplate for Flask RESTX web service'
)

api.add_namespace(chat_ns, path='/chat')