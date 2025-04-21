from sqlalchemy import Column, Integer, String, Enum, Date, Text, DECIMAL, DateTime, TIMESTAMP, func
from .db import Base
import enum

class InsuranceTypeEnum(str, enum.Enum):
    travel = "travel"
    health = "health"

class Quote(Base):
    __tablename__ = "quotes"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String(50), nullable=False)
    insurance_type = Column(Enum(InsuranceTypeEnum), nullable=False)
    destination = Column(String(100), nullable=True)
    start_date = Column(Date, nullable=True)
    end_date = Column(Date, nullable=True)
    age = Column(Integer, nullable=True)
    pre_existing_conditions = Column(Text, nullable=True)
    coverage_amount = Column(DECIMAL(10, 2), nullable=True)
    calculated_premium = Column(DECIMAL(10, 2), nullable=False)
    quote_expiry = Column(DateTime, nullable=True)
    created_at = Column(TIMESTAMP, server_default=func.now())
