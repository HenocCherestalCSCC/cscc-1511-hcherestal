"""
Program Name: Lab15_hcherestal-1.py
Author: Henoc Cherestal
Purpose: This program uses matplotlib and the math library to plot a
heart-shaped math formula. It creates x and y lists from calculated
values, labels the graph, and saves the final plot as an image file.
Starter Code: No starter code was used. I used the Lab 15 instructions
and Chapter 15 concepts from Python Crash Course, 3rd Edition.
Date: May 5, 2026
"""

import math
import matplotlib.pyplot as pltgit 

x_values = []
y_values = []

for number in range(0, 628):
    t = number / 100

    x = 16 * math.sin(t) ** 3
    y = (
        13 * math.cos(t)
        - 5 * math.cos(2 * t)
        - 2 * math.cos(3 * t)
        - math.cos(4 * t)
    )

    x_values.append(x)
    y_values.append(y)
