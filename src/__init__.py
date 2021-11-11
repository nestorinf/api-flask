from flask import Flask
from config.database import db
from flask_sqlalchemy import SQLAlchemy
from flask_compress import Compress
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = db.uri()
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
compress = Compress()
compress.init_app(app)
database = SQLAlchemy(app)

migrate = Migrate(app,database)
from .models import post
# app.logger.debug(database)

# class User(database.Model):
#     id = database.Column(database.Integer, primary_key=True)
#     name = database.Column(database.String(128))
    
# from src.router import *