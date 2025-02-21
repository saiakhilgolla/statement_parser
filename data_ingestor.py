import os
from src.data_processing.data_processor import FileProcessorFactory, DataProcessor
from src.data_categorization.gpt_categorizer import CategorizeTransaction
from src.database.db_config import session_local
from src.utils.path_utils import get_file_list, validate_file_list
from src.utils.file_utils import load_config, is_csv_file


# Load file and database paths from config
config = load_config("config/file_config.json")
file_paths = config['FILE_PATHS']

for csv_file_path in file_paths:
	if not is_csv_file(csv_file_path):
		print(f"Skipping non-CSV file: {csv_file_path}")
		continue

def process_and_categorize_files(file_path, required_columns, db_connection):
    """Process CSV files, categorize transactions, and insert them into the database."""

	file_processor = FileProcessorFactory.get_file_processor('csv', file_path)
	processed_df = DataProcessor(file_processor).process_file()


	# Categorize transactions by passing each row with required cols as a string to categorizer
	categories = [
		CategorizeTransaction(row.to_string()).get_category()
		for _, row in processed_df[required_columns].iterrows()
	]
	processed_df['Category'] = categories
    return (processed_df)


def main():
    print("called main function")
    # Get file paths for debit accounts
    debit_file_paths = get_file_list(CONFIG["debit_path"])
    validated_debit_file_paths = validate_file_list(debit_file_paths)

	# Get file paths for credit accounts
    credit_file_paths = get_file_list(CONFIG["credit_path"])
    validated_credit_file_paths = validate_file_list(credit_file_paths)

    # Required columns for processing
    required_columns = ["Date", "Description", "SubDescription", "TransactionType", "Amount"]

    # Establish database connection
    conn = get_sqlite3_connector(CONFIG["db_path"])

    try:
        process_and_categorize_files(validated_debit_file_paths, required_columns, conn)
        process_and_categorize_files(validated_credit_file_paths, required_columns, conn)
    finally:
        conn.close()

if __name__ == '__main__':
	main()