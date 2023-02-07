from flask import Flask


def init_app(app: Flask):
    @app.get("/")
    def home():
        return {"msg": "Hello Flask"}

    return app
