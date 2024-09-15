from flask import Flask, request, jsonify
from flask_cors import CORS
import mysql.connector
from mysql.connector import Error
from embedding_service import process_resume_and_get_matches, generate_embedding

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}}, supports_credentials=True)

@app.after_request
def add_header(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response

#MySQL configuration
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'password',
    'database': 'database'
}

#Sample cURL request
'''

curl -X POST http://127.0.0.1:5000/add_job \
-H "Content-Type: application/json" \
-d '{
    "title": "Security Engineer",
    "location": "New York City",
    "description": "Analyze and interpret complex data to help companies make better decisions.",
    "company": "Security Inc.",      
    "salary": 250000, 
    "industry": "Data Science",
    "internship": 0,
    "posting_date": "2024-09-15",
    "external_link": "http://datasolutions.com",
    "skills": "Python, R, SQL, Machine Learning"
}'

'''
@app.route('/add_job', methods=['POST'])
def add_job():
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()

        data = request.json
        title = data.get('title')
        location = data.get('location')
        description = data.get('description')
        company = data.get('company')
        salary = data.get('salary')
        industry = data.get('industry')
        internship = data.get('internship')
        posting_date = data.get('posting_date')
        external_link = data.get('external_link')
        skills = data.get('skills')

        embed_string = title + " " + description
        embeddings = generate_embedding(embed_string)
        embeddings = str(embeddings)

        query = """
        INSERT INTO JOB_POSTINGS (title, location, description, company, salary, industry, internship, posting_date, external_link, skills, embeddings)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        data_tuple = (title, location, description, company, salary, industry, internship, posting_date, external_link, skills, embeddings)

        cursor.execute(query, data_tuple)
        connection.commit()

        return jsonify({"message": "Job posting added successfully"}), 201

    except Error as e:
        return jsonify({"error": str(e)}), 500
    
#Sample cURL request
'''
curl -X GET "http://127.0.0.1:5000/search_jobs?company=Data%20Solutions%20Inc.&salary=120000&industry=Data%20Science"
'''
@app.route('/search_jobs', methods=['GET'])
def search_jobs():
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor(dictionary=True)

        company = request.args.get('company')
        title = request.args.get('title')
        salary = request.args.get('salary')
        industry = request.args.get('industry')

        # Base query
        query = "SELECT * FROM JOB_POSTINGS WHERE 1=1"
        params = []

        if company:
            query += " AND company = %s"
            params.append(company)

        if title:
            query += " AND title = %s"
            params.append(title)

        if salary:
            query += " AND salary >= %s"
            params.append(salary)

        if industry:
            query += " AND industry = %s"
            params.append(industry)

        cursor.execute(query, tuple(params))
        results = cursor.fetchall()

        return jsonify(results), 200

    except Error as e:
        return jsonify({"Error searching for jobs": str(e)}), 500

#Sample cURL request
'''
curl -X POST "http://127.0.0.1:5000/upload" \
-H "Content-Type: application/json" \
-d '{"resume": "software", "info": "docker"}'

'''
@app.route('/upload', methods=['POST', 'OPTIONS'])
def upload_to_cohere():
    if request.method == 'OPTIONS':
        # CORS preflight request: respond with necessary headers
        response = jsonify({'message': 'CORS preflight successful'})
        response.headers.add("Access-Control-Allow-Origin", "http://localhost:3000")
        response.headers.add("Access-Control-Allow-Headers", "Content-Type")
        response.headers.add("Access-Control-Allow-Methods", "POST, OPTIONS")
        response.headers.add("Access-Control-Allow-Credentials", "true")
        return response

    # Actual POST request handling
    data = request.json
    skills = data.get('resume')
    resume = data.get('info')

    new_arr = skills + " INFO: " + resume
    #print(new_arr)
    job_list = process_resume_and_get_matches(new_arr)
    payload = []
    for job in job_list:
        del job["embeddings"]
        if job["similarity"] > 0.86:
            payload.append(job)
    print(payload)
    response = jsonify(payload)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response, 200

if __name__ == '__main__':
    app.run(debug=True)
