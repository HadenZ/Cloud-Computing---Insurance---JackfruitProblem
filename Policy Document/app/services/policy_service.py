import os
import httpx
from fastapi import HTTPException
from dotenv import load_dotenv

load_dotenv()  # Ensure environment variables are loaded

POLICY_SERVICE_URL = os.getenv("POLICY_SERVICE_URL")

async def get_policy_details(policy_id: int) -> dict:
    """
    Calls the Policy Management service to get the details of a policy.
    Raises an HTTPException if the policy is not found.
    """
    url = f"{POLICY_SERVICE_URL}/policies/{policy_id}"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
    if response.status_code != 200:
        raise HTTPException(status_code=404, detail="Policy not found")
    return response.json()
