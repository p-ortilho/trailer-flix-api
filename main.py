from flask import Flask, request, jsonify
from flask_cors import CORS
from videos_repository import get_videos, delete_videos, post_videos, put_videos
import os

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def index():
    try:
        return jsonify(
            {
                'status': 'success',
                'message': 'API is working fine',
                'version': '1.0.0'}
            ), 200
    except Exception as e:
        return jsonify(
            {
                'status': 'failed',
                'message': 'Internal server error'}
            ), 500

@app.route('/videos', methods=['GET'])
def get_video():
    try:
        data = get_videos()
        return jsonify(data), 200
    except Exception as e:
        return jsonify(
            {
                'status': 'failed',
                'message': 'Internal server error'}
            ), 500

@app.route('/videos', methods=['POST'])
def post_video():
    try:
        data = request.json
        post_videos(data['titulo'], data['descricao'], data['url'], data['categoria_id'])
        return jsonify(
            {
                'status': 'success',
                'message': 'Video added successfully'}
            ), 201
    except Exception as e:
        return jsonify(
            {
                'status': 'failed',
                'message': 'Internal server error'}
            ), 500

@app.route('/videos/<int:id>', methods=['PUT'])
def put_video(id):
    try:
        data = request.json
        put_videos(id, data['titulo'], data['descricao'], data['url'], data['categoria_id'])
        return jsonify(
            {
                'status': 'success',
                'message': 'Video updated successfully'}
            ), 200
    except Exception as e:
        return jsonify(
            {
                'status': 'failed',
                'message': f'Internal server error{e}'}
            ), 500

@app.route('/videos/<int:id>', methods=['DELETE'])
def delete_video(id):
    try:
        delete_videos(id)
        return jsonify(
            {
                'status': 'success',
                'message': 'Video deleted successfully'}
            ), 200
    except Exception as e:
        return jsonify(
            {
                'status': 'failed',
                'message': 'Internal server error'}
            ), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))