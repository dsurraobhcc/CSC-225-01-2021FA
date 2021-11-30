import csv
from datetime import datetime
import matplotlib.pyplot as plt

filename = 'data/sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header = next(reader)

    dates_sitka, highs_sitka = [], []
    for row in reader:
        try:
            dates_sitka.append(datetime.strptime(row[2], '%Y-%m-%d'))
            highs_sitka.append(int(row[5]))
        except ValueError:
            print('error')

filename = 'data/death_valley_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header = next(reader)

    dates_death_valley, highs_death_valley = [], []
    for row in reader:
        try:
            highs_death_valley.append(int(row[4]))
        except ValueError:
            print('error')
        else:
            dates_death_valley.append(datetime.strptime(row[2], '%Y-%m-%d'))

fig, ax = plt.subplots()
line1, = ax.plot(dates_sitka, highs_sitka, label="Sitka Highs")
line2, = ax.plot(dates_death_valley, highs_death_valley, label="Death Valley Highs")
ax.legend(handles=[line1, line2])

plt.show()