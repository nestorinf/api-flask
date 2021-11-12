from src import app
from flask import jsonify
from src.services.post import Post_Service

@app.route('/posts')
def index():
    posts = Post_Service.get()
    return jsonify({
        "success": True,
        "data": posts
    }), 200