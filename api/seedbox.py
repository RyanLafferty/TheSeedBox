import os, logging
from logging import FileHandler

from flask import Flask, request, flash, url_for, redirect, render_template, jsonify, abort, request, send_from_directory
import flask_sqlalchemy
import flask_restless
from werkzeug.utils import secure_filename
#from flask_restful import reqparse, abort, Api, Resource

#Set up upload folder
UPLOAD_FOLDER = '/uploads'
ALLOWED_EXTENSIONS = set(['csv'])

# Set up application
# ==========================================================================================
application = Flask(__name__)
application.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

application.config['SQLALCHEMY_TRACK_NOTIFICATIONS'] = True
application.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/TheSeedSA'
#application.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/TheSeed'

db = flask_sqlalchemy.SQLAlchemy(application)
#api = Api(application)

# Set up models
# ==========================================================================================
# Create your Flask-SQLALchemy models as usual but with the following two
# (reasonable) restrictions:
#   1. They must have a primary key column of type sqlalchemy.Integer or
#      type sqlalchemy.Unicode.
#   2. They must have an __init__ method which accepts keyword arguments for
#      all columns (the constructor in flask.ext.sqlalchemy.SQLAlchemy.Model
#      supplies such a method, so you don't need to declare a new one).


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
    dateCreated = db.Column(db.DateTime);
    dateScraped = db.Column(db.DateTime);
    price = db.Column(db.Float);
    source = db.Column(db.Unicode(2048))

class GardenFreshBoxes(db.Model):
    __tablename__ = 'GardenFreshBoxes'
    id = db.Column('id', db.Integer, primary_key=True)

class PodOrderForms(db.Model):
    __tablename__ = 'PodOrderForms'
    id = db.Column('id', db.Integer, primary_key=True)
"""
class abc():
    def Test():
        return jsonify(message="Address book created successfully")
"""

# Set up corresponding RESTful API
# ==========================================================================================
# Create the database tables.
db.create_all()

# Create the Flask-Restless API manager.
manager = flask_restless.APIManager(application, flask_sqlalchemy_db=db)

# Create API endpoints, which will be available at /api/<tablename> by
# default. Allowed HTTP methods can be specified as well.
manager.create_api(Users, methods=['GET', 'POST', 'DELETE'])
manager.create_api(Retailers, methods=['GET', 'POST', 'DELETE'])
manager.create_api(Products, methods=['GET', 'POST', 'DELETE'])
manager.create_api(PodOrderForms, methods=['GET', 'POST', 'DELETE'])
manager.create_api(GardenFreshBoxes, methods=['GET', 'POST', 'DELETE'])
#manager.create_api(abc, methods=['GET'])

# Misc. routes
# ==========================================================================================
@application.route("/api/")
def hello():
    return "<h1 style='color:blue'>SEEDBOX API</h1>"


@application.route("/api/upload")
def upload_file():
    return "<h1 style='color:blue'>UPLOAD API</h1>"

@application.route("/api/download")
def download_file():
    return "<h1 style='color:blue'>Download API</h1>"

@application.before_request
def basic_authorize():
    print "hello"

"""
@application.route('/Test')
    def index():
        return jsonify({'Users': Users.query.all()})
"""

"""
@application.route('/Test', methods = ['POST'])
def Test():
   if request.method == 'POST':
      if not request.form['fname']:
         flash('Please enter all the fields', 'error')
      else:
         return redirect('https://seedbox.tk/api/Users')
"""


# ==========================================================================================
if __name__ == "__main__":
    application.run(host='0.0.0.0')
