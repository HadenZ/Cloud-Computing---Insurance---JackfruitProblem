from pydantic import BaseModel
from datetime import datetime

class DocumentCreate(BaseModel):
    policy_id: int
    document_type: str  # For simplicity, we allow free text like "Policy Certificate"

class DocumentOut(BaseModel):
    id: int
    policy_id: int
    document_type: str
    document_url: str
    generated_date: datetime

    class Config:
        orm_mode = True
