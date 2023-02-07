from flask import Flask
from project.api.config import database, mongoengine
from project.api import routes


def create_app():
    app = Flask(__name__)

    database.init_app(app)
    mongoengine.init_app(app)
    routes.init_app(app)

    return app


if __name__ == "__main__":
    create_app().run()
