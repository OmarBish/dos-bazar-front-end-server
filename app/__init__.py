# third-party imports
from flask import Flask
from flask_cors import CORS, cross_origin
from flask_caching import Cache

import os
# local imports
from config import app_config

# Initialize application
app = Flask(__name__, instance_relative_config=True)
cacheConfig = {
    'CACHE_TYPE': 'simple',
    # 'CACHE_TYPE': 'redis',
    # "CACHE_REDIS_URL": os.environ["REDIS_URL"]
}
cache = Cache(app, config=cacheConfig)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

# catalog_servers = ["https://dos-bazar-catalog-server-2.herokuapp.com" , "https://dos-bazar-catalog-server-1.herokuapp.com"]
# order_servers = ["https://dos-bazar-order-server-2.herokuapp.com" , "https://dos-bazar-order-server-1.herokuapp.com"]


catalog_servers = ["https://dos-bazar-catalog-master.herokuapp.com" ,"https://dos-bazar-catalog-read-1.herokuapp.com","https://dos-bazar-catalog-read-2.herokuapp.com"]
order_servers = ["https://dos-bazar-order-server.herokuapp.com","https://dos-bazar-order-server-1.herokuapp.com"]

#get routes
from app import routes

def create_app(config_name):
    app.config.from_pyfile(app_config[config_name])
    return app

