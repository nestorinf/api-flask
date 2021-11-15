from flask import Flask,request
from config.database import db
from flask_sqlalchemy import SQLAlchemy
from flask_compress import Compress
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = db.uri()
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config ['JSON_SORT_KEYS'] = False # order fields sort

compress = Compress()
compress.init_app(app)
database = SQLAlchemy(app)
ma = Marshmallow(app)
migrate = Migrate(app,database)
from .models import post

from src.router import *