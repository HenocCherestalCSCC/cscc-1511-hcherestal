'''
Program Name: Dice Rolling Terms 
Author: Henoc Cherestal 
Purpose: Trying to simulate two dice roll results and print the right gambling term. 
Start Code: None 
Date 02/17/2026
'''

import random 

while True:
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    total = die1 + die2

print(f"\nDie 1: {die1}")
print(f"Die 2: {die2}")
print(f"Total: {total}") 