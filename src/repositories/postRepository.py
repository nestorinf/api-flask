from src.models.post import Post
from src import database
class PostRepository:
    
    def get_all():
        return Post.query.all()
    
    def create_post(name,description):
        post = Post(name,description)
        database.session.add(post)
        database.session.commit()
        return post
    
    def update_post(id,name,description):
        post = Post.query.get(id)
        post.name = name
        post.description = description
        database.session.commit()
        return post
    
    def delete_post(id):
        post = Post.query.get(id)
        database.session.delete(post)
        database.session.commit()
        return post