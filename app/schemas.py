from pydantic import BaseModel

class TransactionCreate(BaseModel):
    account_holder: str | None = None
    amount: float
    type: str
    category: str
    date: str
    notes: str | None = None

class TransactionResponse(TransactionCreate):
    id: int

    class Config:
        from_attributes = True
