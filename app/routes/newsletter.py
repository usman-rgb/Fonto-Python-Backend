from fastapi import APIRouter, Depends, HTTPException
from app.schemas.newsletter import Newsletter
from app.models.newsletter import Newsletter as NewsletterModel
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

@router.post("/newsletter/", response_model=Newsletter)
def subscribe_newsletter(newsletter: Newsletter, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    db_newsletter = NewsletterModel(email=newsletter.email)
    db.add(db_newsletter)
    db.commit()
    db.refresh(db_newsletter)

from fastapi import APIRouter, Depends, HTTPException
from app.schemas.newsletter import Newsletter
from app.models.newsletter import Newsletter as NewsletterModel
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

@router.post("/newsletter/", response_model=Newsletter)
def subscribe_newsletter(newsletter: Newsletter, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    db_newsletter = NewsletterModel(email=newsletter.email)
    db.add(db_newsletter)
    db.commit()
    db.refresh(db_newsletter)

    return db_newsletter
