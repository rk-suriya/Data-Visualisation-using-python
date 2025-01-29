from matplotlib import pyplot as plt
from datetime import datetime
from pathlib import Path
import csv


path = Path("/Users/nivas/Documents/Python/Data Visualization/weather_data/death_valley_2021_simple.csv")
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

for index, column_header in enumerate(header_row):
    print(index, column_header)

data = list(reader)

dates, highs, lows = [], [], []

for row in data:
    try:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        high = int(row[4])
        low = int(row[5])
    except ValueError:
        print(f"Missing data for {current_date}")
    else:
        dates.append(current_date)
        highs.append(high)
        lows.append(low)

fig, ax = plt.subplots()
ax.plot(dates, highs, color='red')
ax.plot(dates, lows, color='blue', alpha=0.5)
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.3)  # Fill the space between the high and low temperatures
ax.set_title("Daily High and Low Temperatures, 2018\nDeath Valley", fontsize=24)
ax.set_xlabel('', fontsize=10)
fig.autofmt_xdate()
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(labelsize=16)  # Set the size of the tick labels

plt.show()
