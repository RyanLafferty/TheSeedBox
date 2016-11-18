import os
from flask import Flask, \
		  send_from_directory
#from flask_restful import Resource, Api

application = Flask(__name__)
#api = Api(application)

@application.route("/api/")
def hello():
    return "<h1 style='color:blue'>SEEDBOX API</h1>"


#class HelloWorld(Resource):
#    def get(self):
#        return {'hello': 'world'}
#
#api.add_resource(HelloWorld, '/')

if __name__ == "__main__":
    application.run(host='0.0.0.0')



