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

if die1 == 1 and die2 ==1:
    print("Snake Eyes")
elif (die1 == 1 and die2 == 2) or (die1 == 2 and die2 == 1):
    print ("Ace Caught a Deuce")
elif die1 == 2 and die2 == 2:
        print("Little Joe from Kokomo")
elif (die1 == 1 and die2 == 4) or (die1 == 4 and die2 == 1):
        print("Little Phoebe")
elif (die1 == 2 and die2 == 3) or (die1 == 3 and die2 == 2):
        print("Little Phoebe")
 elif die1 == 3 and die2 == 3: