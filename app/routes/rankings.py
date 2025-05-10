<<<<<<< HEAD
from fastapi import APIRouter, Depends, HTTPException
from app.database import SessionLocal
from app.auth import get_current_user
from app.schemas.user import User
from app.models.nft import NFT
from app.models.user import User as UserModel
from sqlalchemy.orm import Session
from sqlalchemy import func

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/rankings/", response_model=dict)
def get_rankings(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    # Top Sellers: Users who have sold the most NFTs (based on number of NFTs sold)
    top_sellers = (
        db.query(UserModel, func.count(NFT.id).label("sold_count"))
        .join(NFT, UserModel.id == NFT.owner_id)
        .group_by(UserModel.id)
        .order_by(func.count(NFT.id).desc())
        .limit(10)
        .all()
    )

    # Top Buyers: Users who have bought the most NFTs (based on number of NFTs bought)
    # For simplicity, assuming NFTs are bought via bids or direct purchase, we can use a similar logic
    top_buyers = (
        db.query(UserModel, func.count(NFT.id).label("bought_count"))
        .join(NFT, UserModel.id == NFT.owner_id)
        .group_by(UserModel.id)
        .order_by(func.count(NFT.id).desc())
        .limit(10)
        .all()
    )

    # Format the response
    sellers_data = [
        {"username": seller.username or seller.email, "sold_count": sold_count}
        for seller, sold_count in top_sellers
    ]
    buyers_data = [
        {"username": buyer.username or buyer.email, "bought_count": bought_count}
        for buyer, bought_count in top_buyers
    ]

    return {
        "message": "Rankings data",
        "user_id": current_user.id,  # Fixed: Changed from current_user["id"] to current_user.id
        "top_sellers": sellers_data,
        "top_buyers": buyers_data
=======
from fastapi import APIRouter, Depends, HTTPException
from app.database import SessionLocal
from app.auth import get_current_user
from app.schemas.user import User
from app.models.nft import NFT
from app.models.user import User as UserModel
from sqlalchemy.orm import Session
from sqlalchemy import func

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/rankings/", response_model=dict)
def get_rankings(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    # Top Sellers: Users who have sold the most NFTs (based on number of NFTs sold)
    top_sellers = (
        db.query(UserModel, func.count(NFT.id).label("sold_count"))
        .join(NFT, UserModel.id == NFT.owner_id)
        .group_by(UserModel.id)
        .order_by(func.count(NFT.id).desc())
        .limit(10)
        .all()
    )

    # Top Buyers: Users who have bought the most NFTs (based on number of NFTs bought)
    # For simplicity, assuming NFTs are bought via bids or direct purchase, we can use a similar logic
    top_buyers = (
        db.query(UserModel, func.count(NFT.id).label("bought_count"))
        .join(NFT, UserModel.id == NFT.owner_id)
        .group_by(UserModel.id)
        .order_by(func.count(NFT.id).desc())
        .limit(10)
        .all()
    )

    # Format the response
    sellers_data = [
        {"username": seller.username or seller.email, "sold_count": sold_count}
        for seller, sold_count in top_sellers
    ]
    buyers_data = [
        {"username": buyer.username or buyer.email, "bought_count": bought_count}
        for buyer, bought_count in top_buyers
    ]

    return {
        "message": "Rankings data",
        "user_id": current_user.id,  # Fixed: Changed from current_user["id"] to current_user.id
        "top_sellers": sellers_data,
        "top_buyers": buyers_data
>>>>>>> 4a87b24658b42a81de51559557417a96c9a3e5f7
    }