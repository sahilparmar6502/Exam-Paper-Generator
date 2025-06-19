from flask import Flask
from app.routes.generate_route import generate_bp

app = Flask(__name__)

# Register the Blueprint
app.register_blueprint(generate_bp)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002, debug=True)
