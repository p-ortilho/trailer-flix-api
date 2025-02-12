from flask import Flask, request, jsonify
from videos_repository import get_videos

app = Flask(__name__)

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

if __name__ == '__main__':
    app.run(debug=True)