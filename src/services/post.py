

from src.repositories.postRepository import PostRepository
from src.schemas.PostSchema import PostSchema
from src.validations.create_post_input_schema import CreatePostInputSchema
from src.utils.response import  response
posts_schema = PostSchema(many=True)
post_schema = PostSchema()
  
class Post_Service():
    
    def get():   
        data =  posts_schema.dump( PostRepository.get_all() )
        result = response(data)
        return result
    
    def create(data):
        try:
            name = data['name']
            description = data['description']
            schema_validate = CreatePostInputSchema()
            errors = schema_validate.validate(data)
            if errors:
                response(errors,422)
            result = PostRepository.create_post(name,description)
            response(result,200)
        except:
          pass
      
    def update(data):
        id = data['id']
        name = data['name']
        description = data['description']
        result = PostRepository.update_post(id,name,description)
        return post_schema.dump(result)
    
    def delete(data):
        id  = data['id']
        result = PostRepository.delete_post(id)
        return post_schema.dump(result)