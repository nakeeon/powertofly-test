from challenge.models import db


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80), nullable=False)
    last_name = db.Column(db.String(80), nullable=False)
    username = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), nullable=False)

    def __str__(self):
        return f'<User {self.username}>'

    @classmethod
    def search(cls, **kwargs):
        query = cls.query

        if kwargs.get('first_name'):
            query = query.filter(cls.first_name.ilike(
                f'%{kwargs.get("first_name")}%'))

        if kwargs.get('last_name'):
            query = query.filter(cls.last_name.ilike(
                f'%{kwargs.get("last_name")}%'))

        if kwargs.get('username'):
            query = query.filter(cls.username.ilike(
                f'%{kwargs.get("username")}%'))

        if kwargs.get('email'):
            query = query.filter(cls.email.ilike(f'%{kwargs.get("email")}%'))

        return query
