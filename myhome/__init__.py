import flask
import os 
from flask_sqlalchemy import SQLAlchemy

# gives current directory of this file
basedir = os.path.abspath(os.path.dirname(__file__))

#instance of the Flask class
flaskhw = flask.Flask(__name__)
flaskhw.config.from_mapping(
	SECRET_KEY = 'stuckatthisarea',
	SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db'),
	SQLALCHEMY_TRACK_MODIFICATIONS = False
)

    
db = SQLAlchemy(flaskhw)

from myhome import routes,models