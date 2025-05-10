from fastapi import APIRouter, Depends, HTTPException
from app.schemas.activity import Activity
from app.models.activity import Activity as ActivityModel
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

@router.get("/activities/", response_model=list[Activity])
def get_activities(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    db_activities = db.query(ActivityModel).all()

from fastapi import APIRouter, Depends, HTTPException
from app.schemas.activity import Activity
from app.models.activity import Activity as ActivityModel
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

@router.get("/activities/", response_model=list[Activity])
def get_activities(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    db_activities = db.query(ActivityModel).all()

    return db_activities
