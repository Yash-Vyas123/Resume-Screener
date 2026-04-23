from pdfminer.high_level import extract_text
import os

def parse_resume(pdf_file):
    try:
        text = extract_text(pdf_file)
        return text.strip()
    except Exception as e:
        return f"Error reading PDF: {str(e)}"