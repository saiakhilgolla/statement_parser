from typing import Optional
import pandas as pd
from data_processing.abstract_processor import FileProcessor
from src.utils.file_utils import load_config

config = load_config("configs/file_config.json")


class CSVProcessor(FileProcessor):
	"""This class defines methods used to process CSV files"""
	def __init__(self, file_path:str):
		self.file_path = file_path
		self.df: Optional[pd.DataFrame] = None

	def read_file(self):
		try:
			self.df = pd.read_csv(self.file_path)
		except FileNotFoundError as e:
			raise FileNotFoundError from e
		except Exception as e:
			raise f'Exception {e} was raised'
		return(self.df)

	def validate_dataframe(self):
		if self.df.empty:
			raise f"Dataframe imported from path: [{self.file_path}] is empty. No further processing will be done"
		elif config['REQUIRED_COLS'] not in self.df.columns:
			raise f"One or more of columns {config['REQUIRED_COLS']} are missing"
		else:
			return (self.df)

	def get_account_name(self):
		account_name = [account_name for account_name, keywords in config['ACCOUNT_KEY_WORDS'] if keywords in self.file_path]
		return (account_name[0])

	def add_column(self, col_name, col_value):
		if col_name in self.df.columns:
			raise f'Column {col_name} is already present in the dataframe'

		self.df[col_name] = col_value
		return (self.df)

	def remove_column(self, col_name):
		self.df = self.df.drop(columns=col_name, errors='ignore')  # Avoid errors for missing columns
		return (self.df)

