<<<<<<< HEAD
from fastapi import APIRouter, Depends, HTTPException
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

@router.get("/dashboard/", response_model=dict)
def get_dashboard(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    # Add dashboard logic here
=======
from fastapi import APIRouter, Depends, HTTPException
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

@router.get("/dashboard/", response_model=dict)
def get_dashboard(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    # Add dashboard logic here
>>>>>>> 4a87b24658b42a81de51559557417a96c9a3e5f7
    return {"message": "Dashboard data", "user_id": current_user["id"]}