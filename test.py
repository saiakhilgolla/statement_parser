import sqlite3
import pandas as pd
from src.database.db_operations import fetch_transactions_data

conn = sqlite3.connect("src/database/MonthlyExpenses.db")
#print(fetch_transactions_data(conn))

data = conn.execute("SELECT * FROM Transactions WHERE MonthYear = 'November 2024'")

df = pd.DataFrame(data.fetchall(), columns = ['MonthYear', 'Date', 'Description', 'SubDescription', 'TransactionType', 'Amount', 'AccountType', 'AccountName', 'Category'])
print(df)
df.to_csv('november_data.csv')