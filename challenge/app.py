import os

from flask import Flask
from flask_caching import Cache
from flask_restful import Api

from .models import db
from .resources import users

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

api = Api(app)

cache = Cache(config={
    'CACHE_TYPE': 'RedisCache',
    'CACHE_REDIS_HOST': os.environ.get('REDIS_HOST'),
    'CACHE_REDIS_PORT': os.environ.get('REDIS_PORT'),
})
cache.init_app(app)


api.add_resource(users.Users, '/api/users')
