import os
import mysql.connector
from flask import Flask, request
from flask import jsonify
from flask_cors import CORS

class Connector:
    instance = None

    def __init__(self):
        pass

    def getConnectorInstance():
        if Connector.instance:
            return Connector.instance
        
        Connector.instance = mysql.connector.connect(
            host="localhost",
            user="root",
            password="DeusEreinion0112!",
            database="semhub"
        )

        return Connector.instance



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
        totalReposQuery = 'SELECT count(*) FROM Repositories'
        totalOrgsQuery = 'SELECT count(*) FROM Organizations'
        totalOwnersQuery = 'SELECT count(*) FROM Owners'
        totalIssuesQuery = 'SELECT count(*) FROM Issues'
        return jsonify({
            'totalRepos': 5,
            'totalOrgs': 4,
            'totalOwners': 2,
            'totalIssues': 1,
        })
        return jsonify({
            'totalRepos': cur.execute(totalReposQuery).fetchall()[0],
            'totalOrgs': cur.execute(totalOrgsQuery).fetchall()[0],
            'totalOwners': cur.execute(totalOwnersQuery).fetchall()[0],
            'totalIssues': cur.execute(totalIssuesQuery).fetchall()[0],
        })

    @app.route('/get_repo_by_owner_name')
    def get_repo_by_owner_name(name):
        query = "select name from Repository where owner = %s"
        data = cur.execute(query, name)

    @app.route('/get_repo_by_contributor_name')
    def get_repo_by_contributor_name(name):
        query = 'select R.name from Repository as R join Contributor as C on R.owner = C.user_name where C.user_name = %s'
        data = cur.execute(query, name)
    
    @app.route('/rank_all')
    def rank_all():
        con = Connector.getConnectorInstance()
        cur = con.cursor()
        # data = cur.execute('SELECT repo_name, owner, count(*) as issues, rank() over (ORDER BY count(*) desc) as rank FROM Issues GROUP BY (repo_name, owner)').fetchall()
        return jsonify({
            'rankings': [('bowen', 'bowen', 1, 1), ('bowen', 'bowen', 1, 1)]
        })
        return jsonify({
            'rankings': data,
        })

    return app