import sqlite3
from db_connector import get_sqlite3_connector

def initialize_database(conn:sqlite3.Connection):
	"""Initialize the database and create 'Transactions' table if it already doesn't exist"""
	#initiate cursor object
	cursor = conn.cursor()

	#create Transaction table
	cursor.execute('''
				CREATE TABLE IF NOT EXISTS Transactions (
				MonthYear TEXT,
				Date TEXT,
				Description TEXT,
				SubDescription TEXT,
				TransactionType TEXT,
				Amount REAL,
				AccountType TEXT,
				AccountName TEXT,
				Category TEXT
				)
	''')

	conn.commit()
	conn.close()

def main():
	conn = get_sqlite3_connector("./src/database/MonthlyExpenses.db")
	initialize_database(conn)

if __name__ == "__main__":
	main()