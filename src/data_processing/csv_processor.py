"This module processes csv files with transactions"

import pandas as pd
import re
import logging
from typing import Optional

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class CSVProcessor:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.df: Optional[pd.DataFrame] = None

    def load_csv(self):
        try:
            logging.info(f"Loading CSV file: {self.file_path}")
            self.df = pd.read_csv(self.file_path)
        except FileNotFoundError:
            logging.error(f"File not found: {self.file_path}")
            raise
        except Exception as e:
            logging.error(f"Error loading CSV file: {e}")
            raise
        return self.df

    def drop_columns(self, columns: list):
        if self.df is None:
            raise ValueError("DataFrame is not loaded. Please load the CSV file first.")

        logging.info(f"Dropping columns: {columns}")
        self.df = self.df.drop(columns=columns, errors='ignore')  # Avoid errors for missing columns
        return self.df

    def add_month_col(self):
        if self.df is None:
            raise ValueError("DataFrame is not loaded. Please load the CSV file first.")

        try:
            self.df["Month_Year"] = self.df["Filter"].iloc[0].split(",")[0]
            logging.info("Added Month_Year column.")
        except KeyError:
            logging.error("Column 'Filter' is missing in the DataFrame.")
            raise
        except Exception as e:
            logging.error(f"Error adding Month_Year column: {e}")
            raise
        return self.df

    def add_account_type(self):
        if self.df is None:
            raise ValueError("DataFrame is not loaded. Please load the CSV file first.")

        account_type = "Chequing" if "debit_accounts" in self.file_path else "Credit Card"
        self.df["Account_Type"] = account_type
        logging.info(f"Added Account_Type column with value: {account_type}")
        return self.df

    def add_account_name(self):
        if self.df is None:
            raise ValueError("DataFrame is not loaded. Please load the CSV file first.")

        file_name = self.file_path.split('/')[-1]  # Get file name from path
        match = re.match(r'^(.*?)(?=_\d)', file_name)

        if match:
            account_name = match.group(1)
            self.df["Account_Name"] = account_name
            logging.info(f"Added Account_Name column with value: {account_name}")
        else:
            logging.warning("Could not extract account name from file name.")
        return self.df

    def validate_dataframe(self):
        if self.df is None:
            raise ValueError("DataFrame is not loaded. Please load the CSV file first.")

        logging.info("Validating DataFrame.")
        if self.df.empty:
            logging.warning("The DataFrame is empty.")
        return self.df

# Workflow function to process CSV files
def process_csv(file_path: str) -> pd.DataFrame:
    processor = CSVProcessor(file_path)

    # Load the CSV file
    df = processor.load_csv()

    # Validate the DataFrame
    df = processor.validate_dataframe()

    # Add account type, account name and month/year info
    df = processor.add_account_type()
    df = processor.add_account_name()
    df = processor.add_month_col()

    # Drop columns based on file type
    if "debit_accounts" in file_path:
        df = processor.drop_columns(["Filter"])
    else:
        df = processor.drop_columns(["Filter", "Status"])


    logging.info("CSV processing completed.")
    return df

# Example Usage
""" if __name__ == "__main__":
    file_path = "data/debit_accounts/test.csv"  # Replace with actual path

    try:
        processed_df = process_csv(file_path)
        print(processed_df.head())
    except Exception as e:
        logging.error(f"An error occurred during processing: {e}")
 """