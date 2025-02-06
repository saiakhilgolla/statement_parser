import streamlit as st
import sqlite3
import pandas as pd
from database.db_operations_old import fetch_transactions_data, get_total_monthly_expense
import matplotlib.pyplot as plt
from datetime import datetime


st.title("Expense Tracker Dashboard")

conn = sqlite3.Connection("src/database/MonthlyExpenses.db")
data = get_total_monthly_expense(conn)
df = pd.DataFrame(data, columns=['MonthYear', 'Total_Expense'])

df['MonthYear'] = pd.to_datetime(df['MonthYear'], format='%B %Y')

# Sort by the datetime column (optional)
df = df.sort_values('MonthYear')

# create a line plot
st.line_chart(df, x= 'MonthYear', y='Total_Expense')

#plot with matplotlib
""" fig, ax = plt.subplots()
ax.plot(df.MonthYear, df.Total_Expense)

 ax.set(xlabel='time (s)', ylabel='voltage (mV)',
       title='About as simple as it gets, folks')
#fig.savefig("test.png")
plt.show()
st.pyplot(fig, use_container_width= False) """
