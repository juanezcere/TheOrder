import os
from flask import Flask, g
from flask_cors import CORS
from src import database
from src.helpers.read_json import read_json
# Modules importation
from src.controllers.trucks import trucks
from src.controllers.foods import foods
from src.controllers.orders import orders

app = Flask('TheOrder')

def initialize(path):
    """
    Read the database configuration and register of the endpoints.
    """
    app.config['database'] = read_json(os.path.join(path, 'data', 'database.json'))
    app.register_blueprint(trucks, url_prefix='/trucks')
    app.register_blueprint(foods, url_prefix='/foods')
    app.register_blueprint(orders, url_prefix='/orders')
    cors = CORS(app)

@app.before_request
def before_request():
    g.config = app.config

@app.teardown_request
def teardown_request(response):
    g.config = None
    return response

@app.route('/')
def index():
    """
    Index route.
    """
    return '<h1>The Order API REST!</h1><br><h3>Version: 1.0.20230411</h3>'
