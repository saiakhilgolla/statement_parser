import streamlit as st
import sqlite3
import pandas as pd
from src.database.db_operations import fetch_transactions_data, get_total_monthly_expense
import matplotlib.pyplot as plt

st.title("Expense Tracker Dashboard")

conn = sqlite3.Connection("src/database/MonthlyExpenses.db")
data = get_total_monthly_expense(conn)
df = pd.DataFrame(data, columns=['MonthYear', 'Amount', 'AccountName', 'Category' ])

# create a line plot
st.line_chart(df, x= "MonthYear", y="Amount")

#print(df.MonthYear)
