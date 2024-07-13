#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pickle
from tableau_api_lib import Connection

# Load the trained model
with open('models/arima_model.pkl', 'rb') as f:
    model = pickle.load(f)

# Create a Tableau connection
conn = Connection('https://tableau.example.com', 'username', 'password')

# Create a new workbook
workbook = conn.new_workbook('Sales Analytics')

# Create a new sheet
sheet = workbook.new_sheet('Sales Data')

# Add data to the sheet
sheet.add_data(sales_data_month

