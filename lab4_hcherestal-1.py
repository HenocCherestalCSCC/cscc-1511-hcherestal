'''
Progam Name: Card Dealing 
Author: Henoc Cherestal 
Purpose: Trying to ask the user how many cards to deal, then deal that many 
non-repeating cards and show the hand. 
Starter Code: None 
Date: 02/17/2026
'''

import random

def open_deck(values: list[str], suits: list[str]) -> list[str]: 
    '''Deploy a full deck as strings like 10h ot Jc'''
    deck: list[str] = []
    for value in values:
        for suit in suits:
            deck.append(value + suit)
    return deck 

