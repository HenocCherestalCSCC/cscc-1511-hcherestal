'''
Program Name: Dice Rolling Terms 
Author: Henoc Cherestal 
Purpose: Trying to simulate two dice roll results and print the right gambling term. 
Start Code: None 
Date: 02/17/2026
'''

import random 

while True:
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    total = die1 + die2

    print(f"\nDie 1: {die1}")
    print(f"Die 2: {die2}")
    print(f"Total: {total}") 


    #Possibly try to consolidate, this seems clunky ask Prof if treating the roll as a unordered pair would be better.
    #That seems to be a better solution to writing (a,b) over and over. 

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
        print("Jimmy Hicks from the Sticks")
    elif (die1 == 6 and die2 == 1) or (die1 == 1 and die2 == 6):
        print("Six Ace")
    elif die1 == 4 and die2 == 4:
        print("Eighter from Decatur")
    elif (die1 == 3 and die2 == 6) or (die1 == 6 and die2 == 3):
        print("Nina from Pasadena")
    elif (die1 == 4 and die2 == 5) or (die1 == 5 and die2 == 4):
        print("Nina from Pasadena")
    elif die1 == 5 and die2 == 5:
        print("Puppy Paws")
    elif (die1 == 6 and die2 == 5) or (die1 == 5 and die2 == 6):
        print("Six Five no Jive")
    elif die1 == 6 and die2 == 6:
        print("Boxcars")
    else:
        print("No special term for this roll.") 

    choice = input ("Roll again? (y/n): ").lower() 
    if choice != "y":
        print("Thanks for playing!") 
        break