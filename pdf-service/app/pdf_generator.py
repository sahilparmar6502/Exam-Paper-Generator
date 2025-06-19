from fpdf import FPDF
import os

# Ensure the directory exists for storing PDFs
PDF_DIR = "pdfs"
os.makedirs(PDF_DIR, exist_ok=True)

def generate_pdf(question_paper, filename):
    """
    Generates a PDF file from the given question paper JSON.
    
    Parameters:
    - question_paper (dict): The question paper data
    - filename (str): The name of the generated PDF file

    Returns:
    - str: The path to the generated PDF
    """
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    # Title
    pdf.set_font("Arial", style='B', size=16)
    pdf.cell(200, 10, "Generated Question Paper", ln=True, align='C')
    pdf.ln(10)

    # Exam Type
    pdf.set_font("Arial", style='B', size=14)
    pdf.cell(200, 10, f"Exam Type: {question_paper.get('exam_type', 'N/A')}", ln=True)
    pdf.ln(5)

    # Total Marks
    pdf.cell(200, 10, f"Total Marks: {question_paper.get('total_marks', 'N/A')}", ln=True)
    pdf.ln(5)

    # Questions Section
    pdf.set_font("Arial", size=14)
    for idx, question in enumerate(question_paper.get("questions", []), start=1):
        pdf.multi_cell(0, 10, f"{idx}. {question['text']}")
        pdf.ln(5)

    # Save PDF
    pdf_path = os.path.join(PDF_DIR, filename)
    pdf.output(pdf_path)
    
    return pdf_path
