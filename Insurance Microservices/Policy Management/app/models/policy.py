from sqlalchemy import Column, Integer, String, Date, Enum, ForeignKey
from app.db.database import Base
import enum

class PolicyTypeEnum(str, enum.Enum):
    travel = "travel"
    health = "health"

class Policy(Base):
    __tablename__ = "policies"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer)
    policy_type = Column(Enum(PolicyTypeEnum))
    start_date = Column(Date)
    end_date = Column(Date)
    coverage_amount = Column(Integer)
    premium = Column(Integer)
    status = Column(String(50), default="active")
