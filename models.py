# models.py
from sqlalchemy import Column, Integer, String, Text, Boolean, DateTime, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config import DB_CONFIG

Base = declarative_base()

class JobPosting(Base):
    __tablename__ = 'job_postings'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(255), nullable=False)
    location = Column(String(255))
    description = Column(Text, nullable=False)
    company = Column(String(255))
    salary = Column(String(100))
    industry = Column(String(100))
    internship = Column(Boolean, default=False)
    posting_date = Column(DateTime)
    external_link = Column(String(255))
    skills = Column(String(255))
    embedding = Column(Text)  # Store embeddings as JSON strings

# Database setup
DATABASE_URL = f"mysql+mysqlconnector://{DB_CONFIG['user']}:{DB_CONFIG['password']}@{DB_CONFIG['host']}/{DB_CONFIG['database']}"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
