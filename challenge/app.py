import os

from flask import Flask
from flask_restful import Api

from .common import cache
from .models import db
from .resources import users

app = Flask(__name__)

# Replace "postgres" to "postgresql" to make work on Heroku
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
    'DATABASE_URL').replace("postgres://", "postgresql://", 1)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

api = Api(app)

db.init_app(app)
cache.init_app(app)


api.add_resource(users.Users, '/api/users')
