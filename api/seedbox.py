import os, logging, glob, time, sys
from logging import FileHandler
from werkzeug.utils import secure_filename
from CSVandXLparser import inputSpreadSheet

from flask import Flask, request, flash, url_for, redirect, render_template, jsonify, abort, request, send_from_directory, make_response
import flask_sqlalchemy
import flask_restless
from sqldump import sql_dump
import run_scraper

import auth

#Set up upload folder
UPLOAD_FOLDER = '/uploads'
SESSION_TOKEN = '2f2a061d076f33f6cc5ae217ebb9d38e'
ALLOWED_EXTENSIONS = set(['csv', 'xls', 'xlsx'])
DBNAME = 'TheSeedSA'

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

class Test(db.Model):
    __tablename__ = 'Test'
    id = db.Column(db.Integer, primary_key=True)
    sum = db.Column(db.Integer, default=12)
    de = db.Column(db.Integer)

class Users(db.Model):
    __tablename__ = 'Users'
    id = db.Column(db.Integer, primary_key=True)
    admin = db.Column(db.Boolean)
    fname = db.Column(db.Unicode(256))
    lname = db.Column(db.Unicode(256))
    email = db.Column(db.Unicode(256))
    password = db.Column(db.Unicode(256))
    logintime = db.Column(db.DateTime);


class Retailers(db.Model):
    __tablename__ = 'Retailers'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Unicode(200), unique=True)
    url = db.Column(db.Unicode(256))

class Products(db.Model):
    __tablename__ = 'Products'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Unicode(256))
    quantity = db.Column(db.Integer)
    dateCreated = db.Column(db.DateTime);
    price = db.Column(db.Float);
    source = db.Column(db.Unicode(2048))

class GardenFreshBoxes(db.Model):
    __tablename__ = 'GardenFreshBoxes'
    id = db.Column('id', db.Integer, primary_key=True)

class PodOrderForms(db.Model):
    __tablename__ = 'PodOrderForms'
    id = db.Column('id', db.Integer, primary_key=True)


class Produce(db.Model):
    __tablename__ = 'Produce'
    id = db.Column(db.Integer, primary_key=True)
    item = db.Column(db.Unicode(256), default="")
    location = db.Column(db.Unicode(256), default="")
    amount = db.Column(db.Integer, default=0)
    price = db.Column(db.Float, default=0.0);

class GFB(db.Model):
    __tablename__ = 'GFB'
    id = db.Column(db.Integer, primary_key=True)
    item = db.Column(db.Unicode(256), default="")
    quantity = db.Column(db.Integer, default=0)
    price = db.Column(db.Float, default=0.0)
    total = db.Column(db.Float, default=0.0)
    savings = db.Column(db.Float, default=0.0)

class Scraper(db.Model):
    __tablename__ = 'Scraper'
    id = db.Column(db.Integer, primary_key=True)
    item = db.Column(db.Unicode(256), default="")
    squantity = db.Column(db.Integer, default=0)
    sunitcost = db.Column(db.Float, default=0.0)
    stotal = db.Column(db.Float, default=0.0)
    cquantity = db.Column(db.Integer, default=0)
    cunitcost = db.Column(db.Float, default=0.0)
    ctotal = db.Column(db.Float, default=0.0)
    savings = db.Column(db.Float, default=0.0)

class ScraperSettings(db.Model):
    __tablename__ = 'ScraperSettings'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, default=0)
    metro_enabled = db.Column(db.Integer, default=0)
    nofrills_enabled = db.Column(db.Integer, default=0)
    dayofweek = db.Column(db.Integer, default=0)
    time = db.Column(db.Unicode(256), default="")

class SpreadSheets(db.Model):
    __tablename__ = 'SpreadSheets'
    id = db.Column(db.Integer, primary_key=True)
    ss_name = db.Column(db.Unicode(256), default="")
    json_data = db.Column(db.Text)

    #def __init__(self, **kwargs):
    #    super(SpreadSheets, self).__init__(**kwargs)

    def __init__(self, ss_name, json_data):
        self.ss_name = ss_name
        self.json_data = json_data


# Set up corresponding RESTful API
# ==========================================================================================
# Create the database tables.
db.create_all()

# Create the Flask-Restless API manager.
manager = flask_restless.APIManager(application, flask_sqlalchemy_db=db)

# Create API endpoints, which will be available at /api/<tablename> by
# default. Allowed HTTP methods can be specified as well.
manager.create_api(Users, methods=['GET', 'POST', 'DELETE', 'PUT'])
manager.create_api(Retailers, methods=['GET', 'POST', 'DELETE', 'PUT'])
manager.create_api(Products, methods=['GET', 'POST', 'DELETE' ,'PUT'])
manager.create_api(PodOrderForms, methods=['GET', 'POST', 'DELETE' ,'PUT'])
manager.create_api(GardenFreshBoxes, methods=['GET', 'POST', 'DELETE', 'PUT'])

manager.create_api(Produce, methods=['GET', 'POST', 'DELETE', 'PUT'])
manager.create_api(GFB, methods=['GET', 'POST', 'DELETE', 'PUT'])
manager.create_api(Scraper, methods=['GET', 'POST', 'DELETE', 'PUT'])
manager.create_api(ScraperSettings, methods=['GET', 'POST', 'DELETE', 'PUT'])
manager.create_api(SpreadSheets, methods=['GET', 'POST', 'DELETE', 'PUT'])

# Misc. routes
# ==========================================================================================
@application.route("/api/")
def hello():
    return "<h1 style='color:blue'>SEEDBOX API</h1>"

def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@application.route("/api/run_scraper", methods=['POST'])
def run_scraper():
    print "asdkfjh"
    try:
        run_the_scrapers()#nofrills=request.nofrills,metro=request.metro);
    except:
        return jsonify(sys.exc_info()[0])
    return "OK"


@application.route("/api/upload", methods=['POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return jsonify("no file")
        file = request.files['file']
        # if user does not select file
        if file.filename == '':
            flash('No selected file')
            return jsonify("no selected file")
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file_path = os.path.join(application.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)
            try:
                json_data = inputSpreadSheet(file_path)
            except:
                return jsonify("error parsing file")
            new_entry = SpreadSheets(filename, json_data)
            db.session.add(new_entry)
            db.session.commit()
            return jsonify("Success")

@application.route('/api/download/<filename>', methods=['GET'])
def download(filename):
    return send_from_directory(directory=application.config['UPLOAD_FOLDER'], filename=filename)

@application.route('/api/tables', methods=['GET'])
def get_tables():
    tables = db.metadata.tables.items()
    tableList = []

    for table in tables:
        tableList.append(table[0])

    return jsonify(tablenames=tableList)

@application.route('/api/files', methods=['GET'])
def get_files():
    fileList = []
    os.chdir(UPLOAD_FOLDER)
    for file in glob.glob("*.xls"):
        fileList.append(str(file))
    for file in glob.glob("*.xlsx"):
        fileList.append(str(file))
    for file in glob.glob("*.csv"):
        fileList.append(str(file))
    return jsonify(files=fileList)

@application.route('/api/authenticate', methods=['POST'])
def get_authenticate():

    if request and request.method == 'POST' and request.form['email'] and request.form['password']:
        db_user = Users.query.filter_by(email=request.form['email']).first()

        if db_user is None or db_user.password != request.form['password']:
            return '{"Authentication error"}'

        resp = make_response("Logged in!")
        resp.set_cookie('SESSID', SESSION_TOKEN)
        return resp

    return '{"Requires two parameters, [email=...] and [password=...]"}'

@application.route('/api/backup', methods=['GET'])
def backup_database():
    #os.system('python sqldump.py')
    sql_dump()
    backupName = DBNAME + '.sql'
    return send_from_directory(directory=application.config['UPLOAD_FOLDER'], filename=backupName)

@application.route('/api/SpreadSheets/<filename>', )



@application.before_request
def basic_authorize():
    print "hello"

"""
@application.route('/api/all')
def all():
    return jsonify(Users=str(Users.query.all()))
"""


# ==========================================================================================
if __name__ == "__main__":
    application.run(host='0.0.0.0')
