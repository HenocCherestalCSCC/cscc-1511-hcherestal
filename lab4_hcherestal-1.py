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

def get_card_amt(max_cards: int) -> int: 
    '''Ask until the user enters a valid number between 1 and max amt of cards'''
    #logic test
    while True: 
        user_input: str +input("How many cards do you want!? (1-" + str(max_cards) + "): ").strip() 
