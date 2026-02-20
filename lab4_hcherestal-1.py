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
        user_input: str = input("How many cards do you want!? (1-" + str(max_cards) + "): ").strip() 

        if not user_input.isdigit():
            print("Stop messing around...Please enter a whole number.")
            continue

        count: int = int(user_input)
        if count < 1 or count > max_cards: 
            print("Please enter a number from 1 to " + str(max_cards) + ".")
            continue
        return count 
    
def main() -> None: 
    '''Main function to run the dealign program'''
    values: list[str] = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    suits: list[str] = ["c", "h", "s", "d"]

    deck: list[str] = open_deck(values, suits)
    requested_cards: int = get_card_amt(len(deck))

    #this is where random starts earning its keep, no rpts with random sample

    hand: list[str] = random.sample(deck, k=requested_cards)

    print("\nYour hand:")
    print(hand)

    print("\nTotal cards requested: " + str(requested_cards)) 

if __name__ == "__main__": 
        main()