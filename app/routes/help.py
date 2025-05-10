from fastapi import APIRouter, Depends, HTTPException
from app.schemas.help import HelpQuestion
from app.models.help import HelpQuestion as HelpModel
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

@router.get("/help/{question_id}", response_model=HelpQuestion)
def read_help(question_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    db_help = db.query(HelpModel).filter(HelpModel.id == question_id).first()
    if db_help is None:
        raise HTTPException(status_code=404, detail="Help question not found")

from fastapi import APIRouter, Depends, HTTPException
from app.schemas.help import HelpQuestion
from app.models.help import HelpQuestion as HelpModel
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

@router.get("/help/{question_id}", response_model=HelpQuestion)
def read_help(question_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    db_help = db.query(HelpModel).filter(HelpModel.id == question_id).first()
    if db_help is None:
        raise HTTPException(status_code=404, detail="Help question not found")

    return db_help
