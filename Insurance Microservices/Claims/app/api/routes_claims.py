from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.database import SessionLocal
from app.schemas.claim import ClaimCreate, ClaimOut
from app.crud.claims import create_claim, get_claim, get_all_claims, update_claim_status

router = APIRouter()

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/claims/", response_model=ClaimOut)
def create_new_claim(claim: ClaimCreate, db: Session = Depends(get_db)):
    # Optionally, you could add logic here to verify that the policy exists,
    # for example by calling Policy Management through an inter-service API.
    return create_claim(db, claim)

@router.get("/claims/", response_model=list[ClaimOut])
def list_claims(db: Session = Depends(get_db)):
    return get_all_claims(db)

@router.get("/claims/{claim_id}", response_model=ClaimOut)
def get_claim_by_id(claim_id: int, db: Session = Depends(get_db)):
    claim = get_claim(db, claim_id)
    if not claim:
        raise HTTPException(status_code=404, detail="Claim not found")
    return claim

@router.put("/claims/{claim_id}/status", response_model=ClaimOut)
def change_claim_status(claim_id: int, status: str, db: Session = Depends(get_db)):
    claim = update_claim_status(db, claim_id, status)
    if not claim:
        raise HTTPException(status_code=404, detail="Claim not found")
    return claim
