from fastapi import APIRouter, Depends, HTTPException, status
from app.schemas.user import User, UserCreate, Token, PasswordResetRequest
from app.models.user import User as UserModel
from app.utils.auth import get_password_hash, verify_password, create_access_token, get_current_user
from app.database import SessionLocal
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/register/", response_model=User)
def register(user: UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(UserModel).filter(UserModel.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    hashed_password = get_password_hash(user.password)
    db_user = UserModel(email=user.email, username=user.username, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@router.post("/login/", response_model=Token)
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(UserModel).filter(UserModel.email == form_data.username).first()
    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(status_code=400, detail="Incorrect email or password")
    access_token = create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}

@router.post("/reset-password-request/")
def reset_password_request(request: PasswordResetRequest, db: Session = Depends(get_db)):
    user = db.query(UserModel).filter(UserModel.email == request.email).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    # Add password reset logic here (e.g., send email)
    return {"message": "Password reset link sent"}

@router.get("/me/", response_model=User)
def read_users_me(current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):

from fastapi import APIRouter, Depends, HTTPException, status
from app.schemas.user import User, UserCreate, Token, PasswordResetRequest
from app.models.user import User as UserModel
from app.utils.auth import get_password_hash, verify_password, create_access_token, get_current_user
from app.database import SessionLocal
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/register/", response_model=User)
def register(user: UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(UserModel).filter(UserModel.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    hashed_password = get_password_hash(user.password)
    db_user = UserModel(email=user.email, username=user.username, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@router.post("/login/", response_model=Token)
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(UserModel).filter(UserModel.email == form_data.username).first()
    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(status_code=400, detail="Incorrect email or password")
    access_token = create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}

@router.post("/reset-password-request/")
def reset_password_request(request: PasswordResetRequest, db: Session = Depends(get_db)):
    user = db.query(UserModel).filter(UserModel.email == request.email).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    # Add password reset logic here (e.g., send email)
    return {"message": "Password reset link sent"}

@router.get("/me/", response_model=User)
def read_users_me(current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):

    return current_user
