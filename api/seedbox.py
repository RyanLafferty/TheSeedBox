import os, logging
from logging import FileHandler

from flask import Flask
import flask_sqlalchemy
import flask_restless
from flask_restful import reqparse, abort, Api, Resource


# Set up application
# ==========================================================================================
application = Flask(__name__)

application.config['SQLALCHEMY_TRACK_NOTIFICATIONS'] = True
application.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/TheSeedSA'
#application.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/TheSeed'

db = flask_sqlalchemy.SQLAlchemy(application)
api = Api(application)


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
parser = reqparse.RequestParser()
parser.add_argument('id')

class TestIns(Resource):
    def put(self, id):
        args = parser.parse_args()
        num = {'id': args['id']}
        TODOS[id] = num
        return num, 201
        """

api = Api(app)

TODOS = {
    'todo1': {'task': 'build an API'},
    'todo2': {'task': '?????'},
    'todo3': {'task': 'profit!'},
}


def abort_if_todo_doesnt_exist(todo_id):
    if todo_id not in TODOS:
        abort(404, message="Todo {} doesn't exist".format(todo_id))

parser = reqparse.RequestParser()
parser.add_argument('task')


# Todo
# shows a single todo item and lets you delete a todo item
class Todo(Resource):
    def get(self, todo_id):
        abort_if_todo_doesnt_exist(todo_id)
        return TODOS[todo_id]

    def delete(self, todo_id):
        abort_if_todo_doesnt_exist(todo_id)
        del TODOS[todo_id]
        return '', 204

    def put(self, todo_id):
        args = parser.parse_args()
        task = {'task': args['task']}
        TODOS[todo_id] = task
        return task, 201

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


#implementation of the api's
api.add_resource(Todo, '/todos/<todo_id>')


# Misc. routes
# ==========================================================================================
#@application.route("/api/")
#def hello():
#    return "<h1 style='color:blue'>SEEDBOX API</h1>"


@application.before_request
def basic_authorize():
    print "hello"




# ==========================================================================================
if __name__ == "__main__":
    application.run(host='0.0.0.0')
