from src import app,request
from flask import jsonify
from src.services.post import Post_Service
from src.validations.create_post_input_schema import CreatePostInputSchema
# 
@app.route('/posts')
def index():
    posts = Post_Service.get()
    return posts
    
@app.route('/posts',methods=['POST'])
def create():
    data = request.get_json()
    post = Post_Service.create(data)
    return post
    
@app.route('/posts',methods=['PUT'])
def update():
    data = request.get_json()
    post = Post_Service.update(data)
    return jsonify({
        "success": True,
        "data": post
    }), 200
    
@app.route('/posts',methods=['DELETE'])
def delete():
    data = request.get_json()
    post = Post_Service.delete(data)
    return jsonify({
        "success": True,
        "data": post
    }), 200