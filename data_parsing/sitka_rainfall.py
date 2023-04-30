import csv
import matplotlib.pyplot as plt
from datetime import datetime

filename = 'data\sitka_weather_2018_full.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

     # Get high temperatures from file
    dates, precips = [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        precip = float(row[5])
        dates.append(current_date)
        precips.append(precip)

# Plot the high temperatures.
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.bar(dates, precips, color='blue')

# Format plot.
ax.set_title("Daily Precipitation, 2018", fontsize=24)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Precipitation Amount (in)", fontsize=16)
ax.tick_params(labelsize=16)

plt.show()