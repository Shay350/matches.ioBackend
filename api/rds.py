from flask import Flask, request, jsonify
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)

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

        query = """
        INSERT INTO JOB_POSTINGS (title, location, description, company, salary, industry, internship, posting_date, external_link, skills)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        data_tuple = (title, location, description, company, salary, industry, internship, posting_date, external_link, skills)

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

if __name__ == '__main__':
    app.run(debug=True)
