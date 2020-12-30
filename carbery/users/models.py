from flask_login import UserMixin
from carbery import db


class User(db.Model, UserMixin):
    """ User model """

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(255), nullable=False)
    is_active = db.Column(db.Boolean, default=False)

    # Images
    image_id = db.relationship('Image', backref=db.backref('users'))

    def __repr__(self):
        return '<User %r>' % self.name


class Image(db.Model):
    """ Image model with hashes (md5, sha256) """

    __tablename__ = 'images'

    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(255), unique=True)
    hash_md5 = db.Column(db.String, unique=True)
    hash_sha256 = db.Column(db.String, unique=True)

    # Users
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __repr__(self):
        return '<ID: %r, UserID: %r, MD5: %r, SHA256: %r>' % (
            self.id, self.user_id, self.hash_md5, self.hash_sha256
        )
