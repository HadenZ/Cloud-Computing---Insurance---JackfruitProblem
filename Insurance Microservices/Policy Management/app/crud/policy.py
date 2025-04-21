from sqlalchemy.orm import Session
from app.models.policy import Policy
from app.schemas.policy import PolicyCreate

def create_policy(db: Session, policy_data: PolicyCreate) -> Policy:
    policy = Policy(**policy_data.dict())
    db.add(policy)
    db.commit()
    db.refresh(policy)
    return policy

def get_policies(db: Session):
    return db.query(Policy).all()

def get_policy_by_id(db: Session, policy_id: int):
    return db.query(Policy).filter(Policy.id == policy_id).first()
