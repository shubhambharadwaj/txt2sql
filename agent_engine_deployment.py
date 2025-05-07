import os
import vertexai
from vertexai import agent_engines
from txt2sql.agent import root_agent

PROJECT_ID = os.getenv("BQ_PROJECT_ID")
LOCATION = os.getenv("GOOGLE_CLOUD_LOCATION")
STAGING_BUCKET = os.getenv("STAGING_BUCKET")
print(PROJECT_ID,LOCATION,STAGING_BUCKET)
vertexai.init(project=PROJECT_ID, location=LOCATION, staging_bucket=STAGING_BUCKET)

remote_agent = agent_engines.create(
    agent_engine=root_agent,
    requirements=[
        "google-cloud-aiplatform[agent_engines,langchain]",
        "cloudpickle==3.0.0",
        "pydantic==2.11.2",
        "langgraph",
        "httpx",
    ],
    display_name="txt2sql",
    description="Agent for create SQL queries for natural language input",
)
