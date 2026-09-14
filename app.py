from flask import Flask, jsonify
import os

app = Flask(__name__)


@app.route('/')
def home():
    return '<h1>Flask + Docker</h1>'


@app.route('/api/health')
def health():
    return jsonify({"status": "healthy", "version": os.environ.get("APP_VERSION", "1.0.0")})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
