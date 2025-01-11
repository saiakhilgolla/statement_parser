import sqlite3


def insert_transactions(conn:sqlite3.Connection, row_data:dict):
	#insert new rows into Transactions table
	try:
		with conn:
			conn.executemany('''
							INSERT INTO Transactions VALUES(
							:MonthYear,
							:Date,
							:Description,
							:SubDescription,
							:TransactionType,
							:Amount,
							:AccountType,
							:AccountName,
							:Category)
							''', row_data)
	except sqlite3.IntegrityError:
		print("couldn't add a row twice")
	return(print("Data successfully loaded in to Transactions table"))



""" conn = get_sqlite3_connector("./src/database/MonthlyExpenses.db")
data = {"MonthYear": "November 2024",
		"Date": "2024-11-03",
		"Description": "test",
		"SubDescription": "test_desc",
		"TransactionType": "debit",
		"Amount": 1500,
		"AccountType": "Chequing",
		"AccountName": "preferred Package",
		"Category": "example"}
insert_transactions(conn, data) """