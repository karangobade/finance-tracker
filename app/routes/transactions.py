from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import SessionLocal
from .. import crud, schemas

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/")
def create(tx: schemas.TransactionCreate, db: Session = Depends(get_db)):
    return crud.create_transaction(db, tx)

@router.get("/")
def read_all(db: Session = Depends(get_db)):
    return crud.get_transactions(db)

@router.delete("/{tx_id}")
def delete(tx_id: int, db: Session = Depends(get_db)):
    tx = crud.delete_transaction(db, tx_id)
    if not tx:
        raise HTTPException(status_code=404, detail="Transaction not found")
    return {"message": "Deleted"}
