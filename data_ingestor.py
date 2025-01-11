import os
from src.data_processing.csv_processor import process_csv
from src.data_categorization.gpt_categorizer import CategorizeTransaction
from src.database.db_operations import insert_transactions
from src.utils.path_utils import get_file_list, validate_file_list
from src.database.db_connector import get_sqlite3_connector

# Configuration file paths
CONFIG = {
    "debit_path": "data/debit_accounts",
    "credit_path": "data/credit_accounts",
    "db_path": "src/database/MonthlyExpenses.db",
}

def is_csv_file(file_path):
    """Validate if the file is a CSV file."""
    return file_path.endswith(".csv")

def process_and_categorize_files(file_paths, required_columns, db_connection):
    """Process CSV files, categorize transactions, and insert them into the database."""
    for csv_file_path in file_paths:
        if not is_csv_file(csv_file_path):
            print(f"Skipping non-CSV file: {csv_file_path}")
            continue

        processed_df = process_csv(csv_file_path)

        # Categorize transactions
        categories = [
            CategorizeTransaction(row.to_string()).get_category()
            for _, row in processed_df[required_columns].iterrows()
        ]
        processed_df['category'] = categories

        # Prepare data for database insertion
        data_load = tuple(processed_df.to_dict(orient="records"))
        print(data_load)

        # Insert transactions into the database
        insert_transactions(db_connection, data_load)

def ingest_data():
    # Get file paths for debit accounts
    debit_file_paths = get_file_list(CONFIG["debit_path"])
    validated_debit_file_paths = validate_file_list(debit_file_paths)

	# Get file paths for credit accounts
    credit_file_paths = get_file_list(CONFIG["credit_path"])
    validated_credit_file_paths = validate_file_list(credit_file_paths)

    # Required columns for processing
    required_columns = ["Date", "Description", "Sub-description", "Type of Transaction", "Amount"]

    # Establish database connection
    conn = get_sqlite3_connector(CONFIG["db_path"])

    try:
        process_and_categorize_files(validated_debit_file_paths, required_columns, conn)
        process_and_categorize_files(validated_credit_file_paths, required_columns, conn)
    finally:
        conn.close()

if __name__ == "__ingest_data__":
    ingest_data()