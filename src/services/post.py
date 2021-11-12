from src.repositories.postRepository import PostRepository

class Post_Service():
    def get():
        data = PostRepository.get_all()
        return data