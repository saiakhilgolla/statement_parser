from src.data_processing.csv_processor import process_csv
from src.data_categorization import gpt_categorizer
from src.database.db_operations import insert_transactions
from src.utils.path_utils import get_file_list,  validate_file_list


# define paths for data
TODO: # add them in a config file
debit_path = "data/debit_accounts"
credit_path = "data/credit_accounts"

debit_file_path = get_file_list(debit_path)
validated_debit_file_path = validate_file_list(debit_file_path)

TODO: # ADD A FUNCTION TO VALIDATE IF A FILE IS A CSV FILE
for csv_file_path in validated_debit_file_path:
	processed_df= process_csv(csv_file_path)
	#function to convert row into a csv format as a input to gpt_categorizer
	#add category to the processed_df for each row.
	#function to convert df to dict
	#insert data into sqlite3 database table.

