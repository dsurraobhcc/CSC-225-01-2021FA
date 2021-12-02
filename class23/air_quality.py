'''
Source: https://pandas.pydata.org/docs/getting_started/intro_tutorials/01_table_oriented.html
'''
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data/air_quality_no2.csv', index_col=0, 
    parse_dates=True)
# print(df.head())

# aggregate functions
# print(df['station_london'].max())
# print(df['station_london'].mean())

# filtering 
#print(df[(df['station_antwerp'] > 50) & (df['station_paris'] > 50)])

# df["station_paris"].plot()

df.plot.scatter(x="station_london", y="station_paris", alpha=0.5,
    figsize=(10, 10))

df.plot.box()

df.plot.area(figsize=(12, 4), subplots=True)
plt.show()