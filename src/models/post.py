# from sqlalchemy import Model, Column, Integer, String
from src import database
from sqlalchemy.orm import validates
class Post(database.Model):
    __tablename__ = 'posts'
    
    id = database.Column(database.Integer, primary_key=True)
    name = database.Column(database.String(60))
    description = database.Column(database.String(500))
    
    def __init__(self,name,description):
        self.name = name
        self.description = description
    
