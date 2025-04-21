from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from app.db.database import Base

class Document(Base):
    __tablename__ = "documents"

    id = Column(Integer, primary_key=True, index=True)
    policy_id = Column(Integer, index=True)  # Reference to the policy for which this document is generated
    document_type = Column(String(50))       # e.g., "Policy Certificate"
    document_url = Column(String(255))         # URL or file path where the document is stored
    generated_date = Column(DateTime, default=datetime.utcnow)
