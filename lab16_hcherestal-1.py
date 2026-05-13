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