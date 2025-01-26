'''This script initializes the engine and configures the session to be used for all queries to the tables'''
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Database URL
database_url = "sqlite:///src/database/Expenses.db"

#create the engine
engine = create_engine(database_url, echo = True)

session_local = sessionmaker(bind=engine)