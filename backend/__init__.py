import os
import mysql.connector
from flask import Flask, request
from flask import jsonify
from flask_cors import CORS
from backend.semgrepper.repo_metadata import grab_metadata
from backend.connector import Connector
import re


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    CORS(app)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    @app.route('/summary')
    def summary():
        con = Connector.getConnectorInstance()
        cur = con.cursor()

        pass

    @app.route('/rank_all')
    def rank_all():
        pass

    @app.route('/add_to_queue', methods=['POST'])
    def add_to_queue():

       pass

    @app.route('/compare_repos')
    def compare_repos():
        pass

    @app.route('/top_repos')
    def top_repos():
        pass

    @app.route('/update', methods=['POST'])
    def update():
        pass

    return app

