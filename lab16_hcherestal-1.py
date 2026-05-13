'''
Program Name: Lab16_hcherestal-1.py
Author: Henoc Cherestal
Purpose: I read Ohio unemployment data from OHUR.csv, convert the dates
         and rates into usable values, and create a line plot with matplotlib.
Starter Code: No starter code was used. The OHUR.csv file was provided for
              the lab and comes from the FRED Economic Data.
Date: May 10, 2026
'''

import csv
import datetime
import matplotlib.pyplot as plt

filename = "OHUR.csv"

dates = []
unemployment_rates = []

with open(filename, newline="") as csv_file:
    reader = csv.reader(csv_file)
    header_row = next(reader)

    header_indexes = {}
    for index, column_header in enumerate(header_row):
        header_indexes[column_header] = index

    date_index = header_indexes.get("DATE", 0)
    rate_index = header_indexes.get("OHUR", 1)

    for row in reader:
        try:
            current_date = datetime.datetime.strptime(row[date_index], "%Y-%m-%d")
            unemployment_rate = float(row[rate_index])
        except (ValueError, IndexError):
            continue
        else:
            dates.append(current_date)
            unemployment_rates.append(unemployment_rate)

            plt.style.use("seaborn-v0_8")

fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(dates, unemployment_rates, color="blue")

first_year = dates[0].year
last_year = dates[-1].year

ax.set_title(f"Ohio Unemployment (by Month): {first_year} - {last_year}", fontsize=18)
ax.set_xlabel("Date", fontsize=12)
ax.set_ylabel("Unemp Rate", fontsize=12)

fig.autofmt_xdate()
plt.tight_layout()

plt.savefig("ohio_unemployment.png")
plt.show()