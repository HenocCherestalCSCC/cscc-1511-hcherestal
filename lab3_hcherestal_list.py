'''
Program Name: Lab 3 Part 1 - Trying to Create and Sort a List 
Author: Henoc Cherestal
Purpose: Create a camping list of items, print the number of items, then print the list in alphabetical order
Starter Code: None 
Date: 2/11/2026
''' 

from typing import List 

camping_items: list[str] = [
    "tent",
    "sleeping bags"
    "water bottle"
    "camp stove" 
    "flashlight"
    "first aid kit"
    "matches"
    "map"
    "rain jacket"
    "trail mix"
]

def main() -> None: 
    print(f"Total items: {len(camping_items)}")
    print("Sorted list (A-Z):")
    print(sorted(camping_items))

if __name__ == "__main__": 
    main()