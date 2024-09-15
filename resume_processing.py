# resume_processing.py
import os
from PyPDF2 import PdfReader
import docx

def extract_text_from_pdf(file_path):
    reader = PdfReader(file_path)
    text = ''
    for page in reader.pages:
        text += page.extract_text()
    return text

def extract_text_from_docx(file_path):
    doc = docx.Document(file_path)
    full_text = [para.text for para in doc.paragraphs]
    return '\n'.join(full_text)

def extract_text_from_txt(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def extract_text(file_path, file_type):
    if file_type == 'pdf':
        return extract_text_from_pdf(file_path)
    elif file_type in ['doc', 'docx']:
        return extract_text_from_docx(file_path)
    elif file_type == 'txt':
        return extract_text_from_txt(file_path)
    else:
        raise ValueError('Unsupported file type')
