from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from google.protobuf.timestamp_pb2 import Timestamp
from google.protobuf.json_format import MessageToJson, Parse
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'generated', 'protos'))

import enums_pb2
import job_pb2

app = FastAPI()

class JobBase(BaseModel):
    title: str
    city: str
    description: str
    company_name: str
    salary: float
    industry: int
    experience: int
    posting_date: str  # Expecting ISO 8601 format for simplicity
    external_url: str
    skills: list[str]
    id: str

@app.post("/jobs/")
async def create_job(job: JobBase):
    # Convert Pydantic model to Protobuf message
    job_proto = job_pb2.Job()
    job_proto.title = job.title
    job_proto.city = job.city
    job_proto.description = job.description
    job_proto.company_name = job.company_name
    job_proto.salary = job.salary
    job_proto.industry = job.industry
    job_proto.experience = job.experience

    # Parse posting_date to Timestamp
    timestamp = Timestamp()
    timestamp.FromJsonString(job.posting_date)
    job_proto.posting_date.CopyFrom(timestamp)

    job_proto.external_url = job.external_url
    job_proto.skills.extend(job.skills)
    job_proto.id = job.id

    # Serialize Protobuf message to JSON for response
    job_json = MessageToJson(job_proto)

    return job_json

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
