from challenge.models.users import User
from flask_restful import Resource, fields, marshal_with, reqparse

user_fields = {
    'id':   fields.Integer,
    'first_name': fields.String,
    'last_name': fields.String,
    'email': fields.String,
}

resource_fields = {
    'has_next': fields.Boolean,
    'has_prev': fields.Boolean,
    'page': fields.Integer,
    'total': fields.Integer,
    'items': fields.Nested(user_fields)
}

parser = reqparse.RequestParser()
parser.add_argument('page', type=int)
parser.add_argument('username')
parser.add_argument('first_name')
parser.add_argument('last_name')
parser.add_argument('email')


class Users(Resource):
    @marshal_with(resource_fields)
    def get(self):
        args = parser.parse_args()
        page = args.pop('page', 1)

        return User.search(page, **args)
