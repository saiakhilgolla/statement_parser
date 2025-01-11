import sqlite3

conn = sqlite3.connect("src/database/MonthlyExpenses.db")
cursor = conn.cursor()

data = cursor.execute("SELECT * FROM Transactions")
print(data.fetchall())
