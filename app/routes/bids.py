from fastapi import APIRouter, Depends, HTTPException
from app.schemas.bid import BidCreate, Bid
from app.models.bid import Bid as BidModel
from app.database import SessionLocal
from app.auth import get_current_user
from app.schemas.user import User  # Added this import
from sqlalchemy.orm import Session

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/bids/", response_model=Bid)
def create_bid(bid: BidCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    db_bid = BidModel(nft_id=bid.nft_id, bidder_id=current_user["id"], amount=bid.amount)
    db.add(db_bid)
    db.commit()
    db.refresh(db_bid)
    return db_bid

@router.get("/bids/{bid_id}", response_model=Bid)
def read_bid(bid_id: int, db: Session = Depends(get_db)):
    db_bid = db.query(BidModel).filter(BidModel.id == bid_id).first()
    if db_bid is None:
        raise HTTPException(status_code=404, detail="Bid not found")

    return db_bid
