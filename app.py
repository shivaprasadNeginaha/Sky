from flask import Flask, Blueprint
from flask import Flask, request
from flask.json import jsonify
import requests
from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin
import os
import connexion
from routes import site


# app = Flask(__name__)
url = 'https://api.bittrex.com/api/v1.1/public/getmarketsummarie'
url2 = 'https://api.bittrex.com/api/v1.1/public/getmarketsummary'


def create_app():
    path = os.path.dirname(
        r"C:\Users\40015453\Desktop\New folder (2)\open_api.yml")
    filename = os.path.basename(
        r"C:\Users\40015453\Desktop\New folder (2)\open_api.yml")

    options = {"swagger_ui": True, "swagger_json": True}

    connexion_app = connexion.App(
        __name__, specification_dir=path, options=options)
    connexion_app.add_api(filename, strict_validation=True)
    app = connexion_app
    app.app.register_blueprint(site)
    return app.app


# def create_app():
#     # app = Flask(__name__)
#     # app.register_blueprint(site)
#     # return app