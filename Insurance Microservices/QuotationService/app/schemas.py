from pydantic import BaseModel, Field
from typing import Optional
from datetime import date, datetime
from enum import Enum

class InsuranceTypeEnum(str, Enum):
    travel = "travel"
    health = "health"

# Request schema for creating a quote
class QuoteCreate(BaseModel):
    user_id: str
    insurance_type: InsuranceTypeEnum
    destination: Optional[str] = None
    start_date: Optional[date] = None
    end_date: Optional[date] = None
    age: Optional[int] = None
    pre_existing_conditions: Optional[str] = None
    coverage_amount: Optional[float] = None

# Response schema for returning a quote
class QuoteOut(BaseModel):
    id: int
    user_id: str
    insurance_type: InsuranceTypeEnum
    destination: Optional[str] = None
    start_date: Optional[date] = None
    end_date: Optional[date] = None
    age: Optional[int] = None
    pre_existing_conditions: Optional[str] = None
    coverage_amount: Optional[float] = None
    calculated_premium: float
    quote_expiry: Optional[datetime]
    created_at: datetime

    class Config:
        orm_mode = True
