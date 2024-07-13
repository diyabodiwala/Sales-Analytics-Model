#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
from statsmodels.tsa.arima_model import ARIMA

def update_model(new_data):
    # Load the existing model
    with open('models/arima_model.pkl', 'rb') as f:
        model = pickle.load(f)

    # Append the new data to the existing data
    sales_data = pd.concat([pd.read_csv('data/sales_data.csv'), new_data])

    # Refit the model
    model_fit = model.fit(sales_data)

    # Save the updated model
    with open('models/arima_model.pkl', 'wb') as f:
        pickle.dump(model_fit, f)

    print("Model updated successfully!")

