from sqlalchemy.orm import Session
from datetime import datetime
from app.models.document import Document
from app.schemas.document import DocumentCreate
from app.services.policy_service import get_policy_details
from app.services.pdf_generator import generate_policy_pdf
import asyncio

async def create_document(db: Session, doc_data: DocumentCreate) -> Document:
    # Retrieve policy details from the Policy Management service
    policy_details = await get_policy_details(doc_data.policy_id)
    
    # Generate the PDF with ReportLab using the policy details
    generated_url = generate_policy_pdf(policy_details) 
    
    # Create Document record in the database
    document = Document(
        policy_id=doc_data.policy_id,
        document_type=doc_data.document_type,
        document_url=generated_url,
        generated_date=datetime.utcnow()
    )
    db.add(document)
    db.commit()
    db.refresh(document)
    return document

def create_document_sync(db: Session, doc_data: DocumentCreate) -> Document:
    return asyncio.run(create_document(db, doc_data))

def get_document(db: Session, document_id: int) -> Document:
    return db.query(Document).filter(Document.id == document_id).first()

def get_all_documents(db: Session):
    return db.query(Document).all()