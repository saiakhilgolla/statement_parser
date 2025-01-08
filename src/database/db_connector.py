import sqlite3

def get_sqlite3_connector(path_to_db:str):
	return(sqlite3.connect(path_to_db))