from flask import Flask
from flask_mongoengine import MongoEngine
import os


def init_app(app: Flask):
    db = MongoEngine()
    app.config["MONGODB_SETTINGS"] = {
        "db": "animes",
        "host": os.getenv("DATABASE_URL"),
    }

    db.init_app(app)

    return app
