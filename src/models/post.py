from src import database

class Post(database.Model):
    __tablename__ = 'posts'
    
    id = database.Column(database.Integer, primary_key=True)
    name = database.Column(database.String(60))
    description = database.Column(database.String(500))