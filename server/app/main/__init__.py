import os

from flask import Flask
from flask_jwt_extended import JWTManager

from .config import config_by_name
from flask_cors import CORS


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])
    if config_name == "dev":
        CORS(app)
    return app
