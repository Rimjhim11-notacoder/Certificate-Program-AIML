import pandas as pd
import numpy as np

df = pd.read_csv('stock_market_data.csv')

#print(df.head())
#print(df.columns)

y = df[['Price','Close']] .copy()
print(y.head())
#print(type(y))

z = df['Price']#.values
#print(z)

