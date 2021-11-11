from src import app
from flask import jsonify
from src.services.post import Post_Service

@app.route('/')
def index():
    posts = Post_Service.get()
    return jsonify({
        "message": posts
    }), 200