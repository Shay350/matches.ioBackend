# database.py

import mysql.connector
from mysql.connector import Error
import os
from dotenv import load_dotenv
from contextlib import contextmanager

# Load environment variables from .env file
load_dotenv()

# MySQL configuration using environment variables
db_config = {
    'host': os.getenv('DB_HOST', 'localhost'),
    'user': os.getenv('DB_USER', 'root'),
    'password': os.getenv('DB_PASSWORD', ''),
    'database': os.getenv('DB_NAME', 'database1')
}

@contextmanager
def get_db_connection():
    """Context manager for database connection."""
    connection = None
    try:
        connection = mysql.connector.connect(**db_config)
        yield connection
    except Error as e:
        print(f"Error connecting to MySQL database: {e}")
        raise
    finally:
        if connection and connection.is_connected():
            connection.close()


# In embedding_service.py
from database import get_db_connection

def fetch_job_postings():
    job_postings = []
    try:
        with get_db_connection() as connection:
            cursor = connection.cursor(dictionary=True)
            query = "SELECT * FROM JOB_POSTINGS"
            cursor.execute(query)
            jobs = cursor.fetchall()

            for job in jobs:
                # Process embeddings...
                job_postings.append(job)

            cursor.close()
            ## test print
            ## print (job_postings)
    except Error as e:
        print(f"Error fetching job postings: {e}")
        raise

    return job_postings