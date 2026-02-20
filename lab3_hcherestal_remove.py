'''
Program Name: Lab 3 Part 4 - Removing an item from my list 
Author: Henoc Cherestal 
Purpose: I should import the list for part 3 and remove 'binoculars' from the list, 
then print the completed list. Then I should print how many items I am bringing using len().
Starter Code: None 
Date: 02/17/2026
'''
from typing import List 
from lab3_hcherestal_replace import camping_items as items_from_part3

camping_items: List[str] = items_from_part3.copy()

if "binoculars" in camping_items:
    camping_items.remove("binoculars")

def main() -> None: 
    '''Time to print the list and the total number of items!'''
    print("Final camping list!:")
    print(camping_items)
    print(f"\nI will bring {len(camping_items)} total items on the camping trip.") 

if __name__ == "__main__":
    main()