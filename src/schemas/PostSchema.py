from src import ma,database
from src.models.post import Post

class PostSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Post
        ordered = True
        sqla_session = database.session
        fields = ("id","name","description")