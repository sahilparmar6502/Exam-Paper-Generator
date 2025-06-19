from flask import Flask
from pymongo import MongoClient
from app.routes.question_routes import question_bp

app = Flask(__name__)

# MongoDB Connection
# MONGO_URI = "mongodb://admin:admin123@mongodb:27017/examdb"# Use 'mongodb' as hostname (same as service name in docker-compose)
# client = MongoClient(MONGO_URI)
# db = client["examdb"]  # Database Name
# questions_collection = db["questions"]  # Collection Name

# Register Blueprint
app.register_blueprint(question_bp)
# , url_prefix="/questions"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
