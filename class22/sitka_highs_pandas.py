import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# DataFrame
df = pd.read_csv('data/sitka_weather_07-2018_simple.csv')
highs = df['TMAX']
lows = df['TMIN']
dates = df['DATE'].apply(
    lambda date_str: datetime.strptime(date_str, '%Y-%m-%d')
)

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red', alpha=0.5)
ax.plot(dates, lows, c='blue', alpha=0.5)
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.5)
fig.autofmt_xdate()
plt.show()