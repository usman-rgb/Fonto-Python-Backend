<<<<<<< HEAD
from fastapi import APIRouter, Depends, HTTPException
from app.schemas.collection import CollectionCreate, Collection
from app.models.collection import Collection as CollectionModel
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

@router.post("/collections/", response_model=Collection)
def create_collection(collection: CollectionCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    db_collection = CollectionModel(
        name=collection.name,
        description=collection.description
    )
    db.add(db_collection)
    db.commit()
    db.refresh(db_collection)
    return db_collection

@router.get("/collections/{collection_id}", response_model=Collection)
def read_collection(collection_id: int, db: Session = Depends(get_db)):
    db_collection = db.query(CollectionModel).filter(CollectionModel.id == collection_id).first()
    if db_collection is None:
        raise HTTPException(status_code=404, detail="Collection not found")
=======
from fastapi import APIRouter, Depends, HTTPException
from app.schemas.collection import CollectionCreate, Collection
from app.models.collection import Collection as CollectionModel
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

@router.post("/collections/", response_model=Collection)
def create_collection(collection: CollectionCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    db_collection = CollectionModel(
        name=collection.name,
        description=collection.description
    )
    db.add(db_collection)
    db.commit()
    db.refresh(db_collection)
    return db_collection

@router.get("/collections/{collection_id}", response_model=Collection)
def read_collection(collection_id: int, db: Session = Depends(get_db)):
    db_collection = db.query(CollectionModel).filter(CollectionModel.id == collection_id).first()
    if db_collection is None:
        raise HTTPException(status_code=404, detail="Collection not found")
>>>>>>> 4a87b24658b42a81de51559557417a96c9a3e5f7
    return db_collection