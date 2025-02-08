import os
import unittest
from flask import Flask
from app.main import create_app
from app import blueprint
from flask_cors import CORS

app = create_app(os.getenv('BOILERPLATE_ENV') or 'dev')
CORS(app)
app.register_blueprint(blueprint)


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
