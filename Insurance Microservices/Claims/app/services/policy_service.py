import httpx
from fastapi import HTTPException
import os
from dotenv import load_dotenv

load_dotenv()  # Make sure environment variables are loaded

POLICY_SERVICE_URL = os.getenv("POLICY_SERVICE_URL", "http://localhost:8002/api")

def get_policy_details(policy_id: int) -> dict:
    url = f"{POLICY_SERVICE_URL}/policies/{policy_id}"
    response = httpx.get(url)
    if response.status_code != 200:
        raise HTTPException(status_code=404, detail="Policy not found")
    return response.json()
