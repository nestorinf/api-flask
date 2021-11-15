# from sqlalchemy import Model, Column, Integer, String
from src import database
class Post(database.Model):
    __tablename__ = 'posts'
    
    id = database.Column(database.Integer, primary_key=True)
    name = database.Column(database.String(60))
    description = database.Column(database.String(500))
    
    def __init__(self,name,description):
        self.name = name
        self.description = description
    
    # def create(self):
    #     database.session.add(self)
    #     database.session.commit()
    #     return self