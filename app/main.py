from fastapi import FastAPI
from .database import engine, Base
from .routes import transactions, summary

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(transactions.router, prefix="/transactions", tags=["Transactions"])
app.include_router(summary.router, prefix="/summary", tags=["Summary"])
