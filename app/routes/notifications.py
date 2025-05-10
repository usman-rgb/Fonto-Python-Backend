<<<<<<< HEAD
from fastapi import APIRouter, Depends, HTTPException
from app.schemas.notification import Notification
from app.models.notification import Notification as NotificationModel
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

@router.get("/notifications/", response_model=list[Notification])
def get_notifications(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    db_notifications = db.query(NotificationModel).filter(NotificationModel.user_id == current_user["id"]).all()
=======
from fastapi import APIRouter, Depends, HTTPException
from app.schemas.notification import Notification
from app.models.notification import Notification as NotificationModel
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

@router.get("/notifications/", response_model=list[Notification])
def get_notifications(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    db_notifications = db.query(NotificationModel).filter(NotificationModel.user_id == current_user["id"]).all()
>>>>>>> 4a87b24658b42a81de51559557417a96c9a3e5f7
    return db_notifications