import os
import httpx
from fastapi import HTTPException

USER_SERVICE_URL = os.getenv("USER_SERVICE_URL", "http://localhost:8001")

async def validate_user_exists(user_id: int):
    url = f"{USER_SERVICE_URL}/users/{user_id}"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        if response.status_code != 200:
            raise HTTPException(status_code=404, detail="User not found")
