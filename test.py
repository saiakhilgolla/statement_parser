import sqlite3
from src.database.db_operations import fetch_transactions_data

conn = sqlite3.connect("src/database/MonthlyExpenses.db")
print(fetch_transactions_data(conn))

""" data = cursor.execute("SELECT * FROM Transactions")
print(data.fetchall()) """
