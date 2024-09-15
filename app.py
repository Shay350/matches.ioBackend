# app.py

from flask import Flask, request, jsonify
import os
from werkzeug.utils import secure_filename
from resume_processing import extract_text
from embedding_service import process_resume_and_get_matches
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'pdf', 'doc', 'docx', 'txt'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure the upload folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/upload-resume', methods=['POST'])
def upload_resume():
    if 'resume' not in request.files:
        return jsonify({'error': 'No resume file provided'}), 400
    
    resume_file = request.files['resume']
    file_type = resume_file.filename.split('.')[-1].lower()
    file_path = os.path.join('uploads', resume_file.filename)
    resume_file.save(file_path)
    
    try:
        resume_text = extract_text(file_path, file_type)
        job_matches = process_resume_and_get_matches(resume_text)
        
        # Categorize jobs into tiers
        tier1 = [job for job in job_matches if job['similarity'] >= 0.8]
        tier2 = [job for job in job_matches if 0.5 <= job['similarity'] < 0.8]
        tier3 = [job for job in job_matches if job['similarity'] < 0.5]
        
        response_data = {
            'tier1': tier1,
            'tier2': tier2,
            'tier3': tier3
        }

        return jsonify(response_data)

    except Exception as e:
        return jsonify({'error': str(e)}), 500
if __name__ == '__main__':
    app.run(debug=True)
