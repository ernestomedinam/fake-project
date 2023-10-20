from flask_sqlalchemy import SQLAlchemy
from api.utils import APIException
from base64 import b64encode
import os
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), unique=True, nullable=False)
    salt = db.Column(db.String(120), nullable=False)
    hashed_password = db.Column(db.String(80), unique=False, nullable=False)

    def __init__(self, username, password):
        already = User.query.filter_by(username=username).one_or_none()
        if already is not None:
            raise APIException("user already exists", 400)
        self.salt = b64encode(os.urandom(32)).decode("utf-8") # os.urandom(32).hex()
        self.hashed_password = generate_password_hash(
            f"{password}{self.salt}"
        )
        self.username = username
        db.session.add(self)
        try:
            db.session.commmit()
        except Exception as error:
            db.session.rollback()
            raise APIException(error, 500)

    def __repr__(self):
        return f'<User {self.email}>'

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }