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
        return jsonify({'error': 'No file part'}), 400

    file = request.files['resume']

    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_type = filename.rsplit('.', 1)[1].lower()
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)

        try:
            # Extract text from resume
            resume_text = extract_text(file_path, file_type)

            # Process resume and get job matches
            job_matches = process_resume_and_get_matches(resume_text)

            # Return top N matches
            top_n = 10
            top_matches = job_matches[:top_n]

            # Remove embeddings from response to reduce payload size
            for job in top_matches:
                job.pop('embedding', None)

            return jsonify({'matches': top_matches}), 200

        except Exception as e:
            print('Error:', e)
            return jsonify({'error': 'Failed to process resume'}), 500
        finally:
            # Clean up the uploaded file
            os.remove(file_path)
    else:
        return jsonify({'error': 'Invalid file type'}), 400

if __name__ == '__main__':
    app.run(debug=True)
