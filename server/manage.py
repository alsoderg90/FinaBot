import os
import unittest

from flask_jwt_extended import JWTManager

from app.main import create_app
from app import blueprint

app = create_app(os.getenv('BOILERPLATE_ENV') or 'dev')

app.register_blueprint(blueprint)
app.config["JWT_SECRET_KEY"] = os.getenv('JWT_SECRET_KEY')
JWTManager(app)


# Add custom CLI commands
@app.cli.command('run')
def run():
    """Run the Flask application."""
    app.run()


@app.cli.command('test')
def test():
    """Run unit tests."""
    tests = unittest.TestLoader().discover('app/test', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        exit(0)
    exit(1)


if __name__ == '__main__':
    app.run()
