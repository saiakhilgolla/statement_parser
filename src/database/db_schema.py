from sqlalchemy.ext.declarative import as_declarative
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, Float, ForeignKey, Date
from abc import ABC

# create a base class which the table class will inherit
@as_declarative
class Base():
	pass

class AbstractTable(Base, ABC):
	__table__ : str
	__abstract__ = True # stops sqlalchemy from creating a table for this class

class Categories(AbstractTable):
	__table__ = "categories"

	#Define table schema
	category_id = Column(Integer, primary_key=True, nullable=False, unique=True, index=True)
	category_name = Column(String, unique=True)
	parent_id = Column(Integer, ForeignKey(category_id), nullable=True)

	#Relationships
	transactions =  relationship("Transactions", back_populates= "category")

class Accounts(AbstractTable):
	__table__= "accounts"

	#Define table schema
	account_id = Column(Integer, primary_key=True, nullable=False, unique=True, Index=True)
	account_name = Column(String, unique=True)
	account_type = Column(String)
	account_user = Column(String)

	#Relationship
	transactions  = relationship("Transactions", back_populates="account")

class Transactions(AbstractTable):
	__table__="transactions"

	#Define table schema
	transaction_id = Column(Integer, primary_key=True, nullable=False, unique=True)
	date = Column(Date, nullable=False)
	description = Column(String)
	sub_description = Column(String)
	transaction_type = Column(String)
	amount = Column(Float)
	balance = Column(Float)

	#Foreign Keys
	account_id = Column(Integer, ForeignKey("accounts.account_id"), nullable=False)
	category_id = Column(Integer, ForeignKey("categories.category_id"), nullable=False)

	#Relationships
	account = relationship("Accounts", back_populates="transactions")
	category = relationship("Categories", back_populates="transactions")