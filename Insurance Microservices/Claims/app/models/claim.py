from sqlalchemy import Column, Integer, String, Date, Text
from app.db.database import Base

class Claim(Base):
    __tablename__ = "claims"

    id = Column(Integer, primary_key=True, index=True)
    policy_id = Column(Integer, index=True)  # The ID of the policy this claim belongs to
    user_id = Column(Integer, index=True)    # The ID of the user filing the claim
    claim_amount = Column(Integer)
    claim_date = Column(Date)
    incident_details = Column(Text)
    # The claim status might be "Submitted", "In Review", "Approved", or "Rejected"
    claim_status = Column(String(50), default="Submitted")
