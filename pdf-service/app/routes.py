from flask import Blueprint, request, jsonify, send_file
import uuid
import os
from app.pdf_generator import generate_pdf
from datetime import datetime
import uuid

generate_bp = Blueprint("generate_bp", __name__)

@generate_bp.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "PDF Generator is healthy!"})

PDF_DIR = "pdfs"

@generate_bp.route('/generate_pdf', methods=['POST'])
def generate_paper():
    """
    API to receive question paper data, generate a PDF, and return a download link.
    """
    try:
        question_paper = request.json  # Get JSON data
        if not question_paper:
            return jsonify({"error": "Invalid input, JSON expected"}), 400
    
        # Generate filename with timestamp + short UUID
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")  # Format: YYYYMMDD_HHMMSS
        short_uuid = uuid.uuid4().hex[:6]  # Use first 6 characters of UUID for uniqueness

        filename = f"question_paper_{timestamp}_{short_uuid}.pdf"
        pdf_path = generate_pdf(question_paper, filename)

        # Return download link
        return jsonify({"message": "PDF Generated", "download_url": f"/download_pdf/{filename}"})

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@generate_bp.route('/download_pdf/<filename>', methods=['GET'])
def download_pdf(filename):
    """
    API to download the generated PDF.
    """
    pdf_path = os.path.join(PDF_DIR, filename)
    if not os.path.exists(pdf_path):
        return jsonify({"error": "File not found"}), 404

    return send_file(pdf_path, as_attachment=True)
