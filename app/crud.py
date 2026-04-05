from sqlalchemy.orm import Session
from . import models, schemas

def create_transaction(db: Session, data: schemas.TransactionCreate):
    tx = models.Transaction(**data.dict())
    db.add(tx)
    db.commit()
    db.refresh(tx)
    return tx

def get_transactions(db: Session):
    return db.query(models.Transaction).all()

def delete_transaction(db: Session, tx_id: int):
    tx = db.query(models.Transaction).filter(models.Transaction.id == tx_id).first()
    if tx:
        db.delete(tx)
        db.commit()
    return tx
