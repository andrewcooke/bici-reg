from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func
from flask_security.models import fsqla_v3

db = SQLAlchemy()
fsqla_v3.FsModels.set_db_info(db)


class Role(db.Model, fsqla_v3.FsRoleMixin):
    pass


class User(db.Model, fsqla_v3.FsUserMixin):
    pass


# class User(db.Model):
#
#     __tablename__ = 'user'
#
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.Text, unique=True, nullable=False)
#     email = db.Column(db.Text, unique=True, nullable=False)
#     created = db.Column(db.DateTime(timezone=True), default=func.now())


class Bicycle(db.Model):

    __tablename__ = 'bicycle'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', backref=db.backref('bicycles', lazy=True))
    serial = db.Column(db.Text, nullable=False)
    description = db.Column(db.Text)
    created = db.Column(db.DateTime(timezone=True), default=func.now())
    edited = db.Column(db.DateTime(timezone=True), default=func.now(), onupdate=func.now())


class Sighting(db.Model):

    __tablename__ = 'sighting'
    id = db.Column(db.Integer, primary_key=True)
    bicycle_id = db.Column(db.Integer, db.ForeignKey('bicycle.id'), nullable=False)
    created = db.Column(db.DateTime(timezone=True), default=func.now())
