
# from typing import Callable, Iterator

# from flask.json import jsonify
from src.models.post import Post
from src.schemas.PostSchema import PostSchema
from src import app


class PostRepository:
    
    def get_all():
        # post_schema = PostSchema()
        posts_schema = PostSchema(many=True)

        data = posts_schema.dump(Post.query.all())
 
        return data