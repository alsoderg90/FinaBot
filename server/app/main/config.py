from environs import Env

env = Env()
env.read_env()


class Config:
    GEMINI_API_KEY = env.str('GEMINI_APIKEY')
    GEMINI_API_URL = "https://api.gemini.openai.com/v1/chat"
    DEBUG = False


class DevConfig(Config):
    DEBUG = True,


class TestConfig(Config):
    DEBUG = True,
    TESTING = True


class ProdConfig(Config):
    DEBUG = False

config_by_name = dict(
    dev=DevConfig,
    test=TestConfig,
    prod=ProdConfig
)

GEMINI_API_KEY = Config.GEMINI_API_KEY
GEMINI_API_URL = Config.GEMINI_API_URL
