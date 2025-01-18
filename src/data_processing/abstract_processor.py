from typing import Any
from abc import ABC, abstractmethod
import pandas as pd


class FileProcessor(ABC):
	"""This abstract class defines the methods for other file processor class"""

	@abstractmethod
	def read_file(self) -> pd.DataFrame:
		"reads file and returns the data in a dataframe"
		pass

	@abstractmethod
	def validate_dataframe(self) -> pd.DataFrame:
		"Checks if the df is empty and if required cols are in df"
		pass

	@abstractmethod
	def get_account_name(self) -> str:
		"Finds account name using file name and keywords defined in cofig"
		pass

	@abstractmethod
	def add_column(self, col_name:str, col_value:Any) -> pd.DataFrame:
		"Adds a column to the dataframe"
		pass

	@abstractmethod
	def remove_column(self, col_name:list[str]) -> pd.DataFrame:
		"Removes column from the dataframe"
		pass