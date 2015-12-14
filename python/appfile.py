from flask import Flask, request, session
from flask_restful import Resource, Api
from flask.ext.httpauth import HTTPBasicAuth


app = Flask(__name__)
api = Api(app)
app.debug = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+pg8000://postgres:postgres@localhost/hsg_cloud'
auth = HTTPBasicAuth()
