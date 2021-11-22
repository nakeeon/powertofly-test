import os

from flask import Flask
from flask_caching import Cache
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
api = Api(app)
db = SQLAlchemy(app)

cache = Cache(config={
    'CACHE_TYPE': 'RedisCache',
    'CACHE_REDIS_HOST': os.environ.get('REDIS_HOST'),
    'CACHE_REDIS_PORT': os.environ.get('REDIS_PORT'),
})
cache.init_app(app)
