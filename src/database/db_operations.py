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

def fetch_transactions_data(conn:sqlite3.Connection) -> dict:
	try:
		with conn:
			data = conn.execute("SELECT * FROM Transactions")
	except Exception as e:
		print(f'Exception {e} occured')
	return (data.fetchall())

def get_total_monthly_expense(conn:sqlite3.Connection):
	try:
		with conn:
			data = conn.execute("SELECT MonthYear, SUM(ABS(Amount)) AS Total_Expense FROM Transactions WHERE TransactionType = 'Debit' AND AccountType ='Credit Card' GROUP BY MonthYear")
	except Exception as e:
		print(f'Exception {e} occured')
	return(data.fetchall())
# TODO: ADD FUNCTION TO REMOVE/ DELETE ROWS BASED ON FILTERS
# TODO: ADD FUNCTION TO QUERY DATA FROM DB TABLE

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