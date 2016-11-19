import os, logging
from logging import FileHandler

from flask import Flask
import flask_sqlalchemy
import flask_restless


# Set up application
# ==========================================================================================
application = Flask(__name__)

application.config['SQLALCHEMY_TRACK_NOTIFICATIONS'] = True
application.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/TheSeedSA'
#application.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/TheSeed'

db = flask_sqlalchemy.SQLAlchemy(application)


# Set up models
# ==========================================================================================
# Create your Flask-SQLALchemy models as usual but with the following two
# (reasonable) restrictions:
#   1. They must have a primary key column of type sqlalchemy.Integer or
#      type sqlalchemy.Unicode.
#   2. They must have an __init__ method which accepts keyword arguments for
#      all columns (the constructor in flask.ext.sqlalchemy.SQLAlchemy.Model
#      supplies such a method, so you don't need to declare a new one).
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Unicode(128), unique=True)
    birth_date = db.Column(db.Date)

class Computer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Unicode(128), unique=True)
    vendor = db.Column(db.Unicode(128))
    purchase_time = db.Column(db.DateTime)
    owner_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    owner = db.relationship('User', backref=db.backref('computers',
                                                         lazy='dynamic'))





"""
class Users(db.Model):
    __tablename__ = 'Users'
    id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.Unicode(256))
    lname = db.Column(db.Unicode(256))
    email = db.Column(db.Unicode(256))
    password = db.Column(db.Unicode(256))

class Retailers(db.Model):
    __tablename__ = 'Retailers'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Unicode(256), unique=True)
    url = db.Column(db.Unicode(256))

class Products(db.Model):
    __tablename__ = 'Products'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Unicode(256))
    quantity = db.Column(db.Integer)
    id = db.Column(db.String(80))
    #TODO add remaining columns
    source = db.Column(db.Unicode(2048))

class GardenFreshBoxes(Base):
    __tablename__ = 'GardenFreshBoxes'
    id = Column('id', Integer, primary_key=True)

class PodOrderForms(Base):
    __tablename__ = 'PodOrderForms'
    id = Column('id', Integer, primary_key=True)

"""

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.Unicode(256))
    lname = db.Column(db.Unicode(256))
    email = db.Column(db.Unicode(256))
    password = db.Column(db.Unicode(256))
"""
class Retailers(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Unicode(256), unique=True)
    url = db.Column(db.Unicode(256))

class Products(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Unicode(256))
    quantity = db.Column(db.Integer)
    id = db.Column(db.String(80))
    #TODO
    source = db.Column(db.Unicode(2048))

class GardenFreshBoxes(db.Model):
    id = db.Column(db.Integer, primary_key=True)

class PodOrderForms(db.Model):
    id = db.Column(db.Integer, primary_key=True)"""


# Set up corresponding RESTful API
# ==========================================================================================
# Create the database tables.
db.create_all()

# Create the Flask-Restless API manager.
manager = flask_restless.APIManager(application, flask_sqlalchemy_db=db)

# Create API endpoints, which will be available at /api/<tablename> by
# default. Allowed HTTP methods can be specified as well.
manager.create_api(User, methods=['GET', 'POST', 'DELETE'])
manager.create_api(Computer, methods=['GET'])

manager.create_api(Users, methods=['GET', 'POST', 'DELETE'])
"""
manager.create_api(Retailers, methods=['GET', 'POST', 'DELETE'])
manager.create_api(Products, methods=['GET', 'POST', 'DELETE'])
manager.create_api(PodOrderForms, methods=['GET', 'POST', 'DELETE'])
manager.create_api(GardenFreshBoxes, methods=['GET', 'POST', 'DELETE'])
"""

# Misc. routes
# ==========================================================================================
#@application.route("/api/")
#def hello():
#    return "<h1 style='color:blue'>SEEDBOX API</h1>"


# ==========================================================================================
if __name__ == "__main__":
    application.run(host='0.0.0.0')
