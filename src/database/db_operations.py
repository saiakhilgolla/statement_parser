from sqlalchemy.orm import Session
from database.db_schema import Transactions, Categories, Accounts
from pydantic import BaseModel, Field
from datetime import date
from typing import Optional

# class to enforce input schema before adding data into Transactions table
class TransactionsInput(BaseModel):
    date: date
    description: str
    sub_description: str
    transaction_type: str
    amount: float
    balance: float
    account_id: int
    category_id: int

#class to enforce input schema before adding input into accounts table
class AccountsInput (BaseModel):
    account_name: str
    account_type: str
    account_user: str

class CategoryInput(BaseModel):
    category_name: str
    parent_id: Optional[str] = None

# Add a new transaction
def add_transaction(db: Session, transaction_data: TransactionsInput):
    new_transaction = Transactions(**transaction_data.model_dump()) #converts TransactionsInput instance to a dict
    db.add(new_transaction)
    db.commit()
    db.refresh(new_transaction)
    return new_transaction

# Get all transactions
def get_transactions(db: Session):
    return db.query(Transactions).all()


# Update an existing transaction
def update_transaction(db: Session, transaction_id: int, update_data: dict):
    transaction = db.query(Transactions).filter(Transactions.transaction_id == transaction_id).first()
    if not transaction:
        return None
    for key, value in update_data.items():
        setattr(transaction, key, value)
    db.commit()
    db.refresh(transaction)
    return transaction

# Delete a transaction
def delete_transaction(db: Session, transaction_id: int):
    transaction = db.query(Transactions).filter(Transactions.transaction_id == transaction_id).first()
    if not transaction:
        return None
    db.delete(transaction)
    db.commit()
    return transaction
