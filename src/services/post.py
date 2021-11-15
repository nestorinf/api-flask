from src.repositories.postRepository import PostRepository
from src.schemas.PostSchema import PostSchema

posts_schema = PostSchema(many=True)
post_schema = PostSchema()
  
class Post_Service():
    
    def get():   
        data =  posts_schema.dump( PostRepository.get_all() )
        return data
    
    def create(data):
        name = data['name']
        description = data['description']
        result = PostRepository.create_post(name,description)
        return post_schema.dump(result)
    
    def update(data):
        id = data['id']
        name = data['name']
        description = data['description']
        result = PostRepository.update_post(id,name,description)
        return post_schema.dump(result)
    
    def delete(data):
        id = data['id']
        result = PostRepository.delete_post(id)
        return post_schema.dump(result)