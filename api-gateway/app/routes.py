import requests
from flask import Blueprint, jsonify, request, send_file
import io

api_routes = Blueprint('api_routes', __name__)

QUESTION_SERVICE_URL = "http://question-service:5001"  # Docker service name
GENERATION_SERVICE_URL = "http://generation-service:5002"
PDF_SERVICE_URL = "http://pdf-service:5003"

@api_routes.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "API Gateway is healthy!"})

@api_routes.route('/question-list', methods=['GET'])
def get_questions():
    """Forward request to question-service"""
    response = requests.get(f"{QUESTION_SERVICE_URL}/question-list")
    return jsonify(response.json()), response.status_code


@api_routes.route('/generate_paper', methods=['POST'])
def generate_paper():
    """Forward request to generation-service."""
    try:
        response = requests.post(f"{GENERATION_SERVICE_URL}/generate_paper", json=request.json)
        response.raise_for_status()  # Raises an error for 4xx or 5xx responses
        return jsonify(response.json()), response.status_code
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500
    
@api_routes.route('/generate_pdf', methods=['POST'])
def generate_pdf():
    """Forward the request to pdf-service to generate a PDF"""
    response = requests.post(f"{PDF_SERVICE_URL}/generate_pdf", json=request.json)
    return jsonify(response.json()), response.status_code

@api_routes.route('/download_pdf/<filename>', methods=['GET'])
def download_pdf(filename):
    """
    Forward the request to the PDF microservice.
    """
    pdf_service_url = f"{PDF_SERVICE_URL}/download_pdf/{filename}"
    response = requests.get(pdf_service_url, stream=True)

    if response.status_code == 200:
        # Convert response content into a file-like object
        file_stream = io.BytesIO(response.content)
        return send_file(file_stream, as_attachment=True, download_name=filename, mimetype='application/pdf')
    
    return jsonify({"error": "File not found"}), response.status_code


# @api_routes.route('/check-health', methods=['GET'])
# def get_questions():
#     """Forward request to question-service"""
#     response = requests.get(f"{GENERATION_SERVICE_URL}/health-generation")
#     return jsonify(response.json()), response.status_code


