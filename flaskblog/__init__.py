from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# from models import User, Port

import os
from datetime import datetime, timedelta

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SECRET_KEY'] = '76b6305f37018078c544578c93405462' #took it with secrets.token_hex(16) from secrets module
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir,'site.db')
db = SQLAlchemy(app)

#in order not to get error of circular import we should input routes that uses app after the creation of app
from flaskblog import routes