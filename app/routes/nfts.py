<<<<<<< HEAD
from fastapi import APIRouter, UploadFile, File, Depends, HTTPException
from app.schemas.nft import NFTCreate, NFT
from app.models.nft import NFT as NFTModel
from app.utils.xrpl_utils import XRPLClient
from app.utils.ipfs import upload_to_ipfs
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

@router.post("/nfts/", response_model=NFT)
async def create_nft(
    nft: NFTCreate,
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    ipfs_hash = await upload_to_ipfs(file.file)
    xrpl_client = XRPLClient()
    token_id = xrpl_client.mint_nft(current_user["id"], ipfs_hash)

    db_nft = NFTModel(
        name=nft.name,
        description=nft.description,
        ipfs_hash=ipfs_hash,
        xrpl_token_id=token_id,
        collection_id=nft.collection_id,
        owner_id=current_user["id"]
    )
    db.add(db_nft)
    db.commit()
    db.refresh(db_nft)
    return db_nft

@router.get("/nfts/{nft_id}", response_model=NFT)
def read_nft(nft_id: int, db: Session = Depends(get_db)):
    db_nft = db.query(NFTModel).filter(NFTModel.id == nft_id).first()
    if db_nft is None:
        raise HTTPException(status_code=404, detail="NFT not found")
=======
from fastapi import APIRouter, UploadFile, File, Depends, HTTPException
from app.schemas.nft import NFTCreate, NFT
from app.models.nft import NFT as NFTModel
from app.utils.xrpl_utils import XRPLClient
from app.utils.ipfs import upload_to_ipfs
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

@router.post("/nfts/", response_model=NFT)
async def create_nft(
    nft: NFTCreate,
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    ipfs_hash = await upload_to_ipfs(file.file)
    xrpl_client = XRPLClient()
    token_id = xrpl_client.mint_nft(current_user["id"], ipfs_hash)

    db_nft = NFTModel(
        name=nft.name,
        description=nft.description,
        ipfs_hash=ipfs_hash,
        xrpl_token_id=token_id,
        collection_id=nft.collection_id,
        owner_id=current_user["id"]
    )
    db.add(db_nft)
    db.commit()
    db.refresh(db_nft)
    return db_nft

@router.get("/nfts/{nft_id}", response_model=NFT)
def read_nft(nft_id: int, db: Session = Depends(get_db)):
    db_nft = db.query(NFTModel).filter(NFTModel.id == nft_id).first()
    if db_nft is None:
        raise HTTPException(status_code=404, detail="NFT not found")
>>>>>>> 4a87b24658b42a81de51559557417a96c9a3e5f7
    return db_nft