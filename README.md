## Finance Tracker Backend

A simple backend system built using FastAPI to manage financial records like income and expenses.
This project focuses on clean structure, basic API design, and handling financial data efficiently.

🚀 Features
Create, update, delete financial transactions
View all transactions
Filter records by type, category, or date
Summary of:
Total income
Total expenses
Current balance
Basic role-based logic (viewer, analyst, admin)
Input validation and proper error handling
SQLite database for storage


## How to Run

1. Clone the repository
2. Install dependencies:
   pip install -r requirements.txt

3. Run server:
   uvicorn app.main:app --reload

4. Open in browser:
   http://127.0.0.1:8000/docs

  ## API Endpoints
Transactions
POST /transactions/ → Create transaction
GET /transactions/ → Get all transactions
PUT /transactions/{id} → Update transaction
DELETE /transactions/{id} → Delete transaction
