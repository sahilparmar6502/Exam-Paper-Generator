from flask import Blueprint, request, jsonify
from app.paper_generator import generate_unique_papers
import requests
import random

generate_bp = Blueprint("generate_bp", __name__)

QUESTION_SERVICE_URL = "http://question-service:5001"

def get_questions(exam_type, topics,difficulty):
    """Fetch questions from question-service based on exam_type and topics."""
    params = {
        "exam_type": exam_type,
        "topics": ",".join(topics) if topics else "",
        "difficulty": difficulty
    }

    try:
        response = requests.get(f"{QUESTION_SERVICE_URL}/fetch-question", params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching questions: {e}")
        return []

@generate_bp.route('/generate_paper', methods=['POST'])
def generate_paper():
    """Generate unique question papers and return as JSON."""

    data = request.get_json()
    print("Received Request Data:", data)  # Debugging

    if not data:
        return jsonify({"error": "Invalid request, parameters required"}), 400
    
    exam_type = data.get("exam_type", "Theory")
    total_marks = data.get("total_marks", 50)
    topics = data.get("topics", [])
    difficulty = data.get("difficulty", "Medium")  # Missing in original code
    num_papers = data.get("num_papers", 3)

    if not topics:
        return jsonify({"error": "At least one topic must be specified"}), 400
    
    questions = get_questions(exam_type, topics,difficulty)
    random.shuffle(questions)

    papers = generate_unique_papers(questions, total_marks, num_papers)
    return jsonify({"papers": papers}), 200



#@generate_bp.route('/health-generation', met7hods=['GET'])
# def health_check():
#     return jsonify({"status": "Generation API is healthy!"})