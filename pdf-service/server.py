from flask import Flask
from app.routes import generate_bp
from flask_cors import CORS

app = Flask(__name__)
CORS(app) 

# Register blueprint
app.register_blueprint(generate_bp)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5003, debug=True)
