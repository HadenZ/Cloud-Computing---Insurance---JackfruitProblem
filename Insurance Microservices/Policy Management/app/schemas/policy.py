from pydantic import BaseModel
from datetime import date
from enum import Enum

class PolicyType(str, Enum):
    travel = "travel"
    health = "health"

class PolicyCreate(BaseModel):
    user_id: int
    policy_type: PolicyType
    start_date: date
    end_date: date
    coverage_amount: int
    premium: int

class PolicyOut(BaseModel):
    id: int
    user_id: int
    policy_type: PolicyType
    start_date: date
    end_date: date
    coverage_amount: int
    premium: int
    status: str

    class Config:
        orm_mode = True
