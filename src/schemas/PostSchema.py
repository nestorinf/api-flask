from src import ma
from src.models.post import Post

class PostSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Post
        ordered = True
        fields = ("id","name","description")