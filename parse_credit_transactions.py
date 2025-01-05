import pandas as pd

df = pd.read_csv("data/Scotiabank_Gold_Amex_Card_9017_113024.csv")
print(df)

def add_month_col(file_path: str):
	#read csv file
	transactions_df = pd.read_csv(file_path)

	#create a new column for month and year
	transactions_df["Month_Year"] = transactions_df["Filter"][0].split(",")[0]

	#remove unnecessary columns
	transactions_df.drop(columns = 'Filter')

	return transactions_df.drop(columns = ['Filter', 'Status'])