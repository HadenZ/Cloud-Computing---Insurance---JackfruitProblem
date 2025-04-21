from sqlalchemy.orm import Session
from app.models.claim import Claim
from app.schemas.claim import ClaimCreate

def create_claim(db: Session, claim_data: ClaimCreate) -> Claim:
    claim = Claim(**claim_data.dict())
    db.add(claim)
    db.commit()
    db.refresh(claim)
    return claim

def get_claim(db: Session, claim_id: int) -> Claim:
    return db.query(Claim).filter(Claim.id == claim_id).first()

def get_all_claims(db: Session):
    return db.query(Claim).all()

def update_claim_status(db: Session, claim_id: int, new_status: str) -> Claim:
    claim = get_claim(db, claim_id)
    if claim:
        claim.claim_status = new_status
        db.commit()
        db.refresh(claim)
    return claim
