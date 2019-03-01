import os
import sys
from flask import Flask, g
from config import BaseConfig
from flask_login import LoginManager
from flask_pymongo import PyMongo


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object('config.BaseConfig')
    login = LoginManager()

    with app.app_context():
        from . import views
        from . import auth
        login.init_app(app)
        mongo = PyMongo(app, app.config['MONGO_URI'])
        app.register_blueprint(views.main)
        app.register_blueprint(admin.admin)

        return app