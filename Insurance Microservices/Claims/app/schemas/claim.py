from pydantic import BaseModel
from datetime import date

class ClaimCreate(BaseModel):
    policy_id: int
    user_id: int
    claim_amount: int
    claim_date: date
    incident_details: str

class ClaimOut(BaseModel):
    id: int
    policy_id: int
    user_id: int
    claim_amount: int
    claim_date: date
    incident_details: str
    claim_status: str

    class Config:
        orm_mode = True
