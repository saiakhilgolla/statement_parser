import pandas as pd

#df = pd.read_csv("data/november_2024.csv")

'''
CSV parsing before categorization
1. add new column for the month and year
2. add the account information - account type and account/credit card name
3. Bank info - bank name

'''
# add new column for the month and year


def add_month_col(file_path: str):
	#read csv file
	transactions_df = pd.read_csv(file_path)

	#create a new column for month and year
	transactions_df["Month_Year"] = transactions_df["Filter"][0].split(",")[0]

	return transactions_df.drop(columns = 'Filter')



parsed_csv = add_month_col("data/november_2024.csv")
print(parsed_csv)