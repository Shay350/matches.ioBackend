from flask import Flask, request, jsonify
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)

#MySQL configuration
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'password',
    'database': 'database1'
}

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

if __name__ == '__main__':
    app.run(debug=True)
