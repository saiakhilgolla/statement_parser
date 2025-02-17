from db_config import engine, Base

def initialize_db():
	# TODO: Add a check to see if the tables already exist.
	# TODO: Add a flag to hard delete existing tables and create new ones.
	#create tables
	Base.metadata.create_all(engine)
	print("Tables created successfully")

if __name__ == "__main__":
	#initialize tables
	initialize_db()
