from flask import Flask, jsonify
from app.routes import api_routes
from flask_cors import CORS

app = Flask(__name__)

# Register API routes
app.register_blueprint(api_routes)
CORS(app) 

@app.route('/')
def home():
    return jsonify({"message": "API Gateway is running!"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)