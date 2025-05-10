from fastapi import APIRouter, Depends, HTTPException
from app.schemas.blog import Blog
from app.models.blog import Blog as BlogModel
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

@router.get("/blogs/{blog_id}", response_model=Blog)
def read_blog(blog_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    db_blog = db.query(BlogModel).filter(BlogModel.id == blog_id).first()
    if db_blog is None:
        raise HTTPException(status_code=404, detail="Blog not found")

    return db_blog
