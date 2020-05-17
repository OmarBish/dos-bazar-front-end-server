# third-party imports
from flask import Flask
from flask_cors import CORS, cross_origin
from flask_caching import Cache


# local imports
from config import app_config

# Initialize application
app = Flask(__name__, instance_relative_config=True)
cache = Cache(app, config={'CACHE_TYPE': 'simple'})
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

# catalog_servers = ["https://dos-bazar-catalog-server-2.herokuapp.com" , "https://dos-bazar-catalog-server-1.herokuapp.com"]
# order_servers = ["https://dos-bazar-order-server-2.herokuapp.com" , "https://dos-bazar-order-server-1.herokuapp.com"]


catalog_servers = ["https://dos-bazar-catalog-server.herokuapp.com" ]
order_servers = ["https://dos-bazar-order-server.herokuapp.com"]

#get routes
from app import routes

def create_app(config_name):
    app.config.from_pyfile(app_config[config_name])
    return app

