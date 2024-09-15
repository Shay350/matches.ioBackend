# embedding_service.py
import json
import numpy as np
from dotenv import load_dotenv
import os

from sklearn.metrics.pairwise import cosine_similarity
import cohere
from config import COHERE_API_KEY
from database import SessionLocal
from models import JobPosting
print(f"COHERE_API_KEY: {COHERE_API_KEY}")

# Initialize Cohere client
co = cohere.Client(COHERE_API_KEY)

def generate_embedding(text):
    response = co.embed(
        texts=[text],
        model='embed-multilingual-v2.0',
        truncate='RIGHT'
    )
    return response.embeddings[0]

def get_job_postings_with_embeddings(session):
    jobs = session.query(JobPosting).all()
    job_postings = []

    for job in jobs:
        if job.embedding:
            embedding = json.loads(job.embedding)
        else:
            # Generate embedding for the job description
            embedding = generate_embedding(job.description)
            # Save the embedding back to the database
            job.embedding = json.dumps(embedding)
            session.commit()

        job_postings.append({
            'id': job.id,
            'title': job.title,
            'description': job.description,
            'embedding': embedding
        })

    return job_postings

def process_resume_and_get_matches(resume_text):
    # Generate embedding for the resume text
    resume_embedding = generate_embedding(resume_text)
    resume_embedding_np = np.array(resume_embedding).reshape(1, -1)

    # Fetch job postings and their embeddings
    session = SessionLocal()
    job_postings = get_job_postings_with_embeddings(session)

    # Prepare job embeddings
    job_embeddings = np.array([job['embedding'] for job in job_postings])

    # Compute cosine similarities
    similarities = cosine_similarity(resume_embedding_np, job_embeddings)[0]

    # Attach similarities to job postings
    for idx, job in enumerate(job_postings):
        job['similarity'] = float(similarities[idx])

    # Sort job postings by similarity
    job_postings.sort(key=lambda x: x['similarity'], reverse=True)

    # Close the session
    session.close()

    return job_postings
