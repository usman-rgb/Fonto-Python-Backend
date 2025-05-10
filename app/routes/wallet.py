<<<<<<< HEAD
from fastapi import APIRouter, Depends, HTTPException
from app.schemas.wallet import Wallet
from app.models.wallet import Wallet as WalletModel
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

@router.get("/wallet/", response_model=Wallet)
def get_wallet(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    db_wallet = db.query(WalletModel).filter(WalletModel.user_id == current_user["id"]).first()
    if db_wallet is None:
        raise HTTPException(status_code=404, detail="Wallet not found")
=======
from fastapi import APIRouter, Depends, HTTPException
from app.schemas.wallet import Wallet
from app.models.wallet import Wallet as WalletModel
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

@router.get("/wallet/", response_model=Wallet)
def get_wallet(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    db_wallet = db.query(WalletModel).filter(WalletModel.user_id == current_user["id"]).first()
    if db_wallet is None:
        raise HTTPException(status_code=404, detail="Wallet not found")
>>>>>>> 4a87b24658b42a81de51559557417a96c9a3e5f7
    return db_wallet