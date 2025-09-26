# function to read a walmart.csv file
# add a new column income_category based on income, if income > 30000 then 'Low'
# if income between 30000 and 70000 then 'Medium', if income > 70000 then 'High'
# return the dataframe
import pandas as pd

def read_walmart_data(file_path):
    df = pd.read_csv(file_path)
    df = df.dropna(subset=['product_id'])
    df['income_category'] = pd.cut(df['income'], bins=[0, 30000, 70000, float('inf')],
                                   labels=['Low', 'Medium', 'High'])
    return df