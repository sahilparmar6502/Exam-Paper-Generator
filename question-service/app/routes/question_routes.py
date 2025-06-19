from flask import Blueprint, jsonify, request
from pymongo import MongoClient

question_bp = Blueprint("question_bp", __name__)

# MongoDB Connection with Authentication
MONGO_URI = "mongodb://admin:admin123@mongodb:27017/exam_db?authSource=admin"

client = MongoClient(MONGO_URI)
db = client["examdb"]
questions_collection = db["questions"]

# API to Get All Questions
@question_bp.route("/question-list", methods=["GET"])
def get_questions():
    questions = list(questions_collection.find({}, {"_id": 0}))  # Fetch all documents & exclude `_id`
    return jsonify(questions)

# API to Add a Question
@question_bp.route("/add", methods=["POST"])
def add_question():
    data = request.json  # Get JSON data from request
    questions_collection.insert_one(data)  # Insert into MongoDB
    return jsonify({"message": "Question added successfully!"})


@question_bp.route("/fetch-question", methods=["GET"])
def fetch_questions():
    """Fetch questions based on exam_type and topics."""
    exam_type = request.args.get("exam_type", "Theory")
    topics = request.args.get("topics", "")
    difficulty = request.args.get("difficulty","Medium")

    topics_list = topics.split(",") if topics else []

    query = {"Exam Type": exam_type}
    query = {"Difficulty":difficulty}
    if topics_list:
        query["Topic"] = {"$in": topics_list}

    try:
        questions = list(questions_collection.find(query, {"_id": 0}))
        return jsonify(questions)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

