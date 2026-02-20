''' 
Program Name: Lab 3 Part 3 - Replace Item in my List 
Author: Henoc Cherestal 
Purpsoe: Supposed to import the list from Lab Part 2, then replace one middle item with 'binoculars,' 
then use a notation slice to print the items before binoculars, binoculars, and the items after binoculars.
Starter Code: None 
Date 02/16/2026
'''
from typing import List 
from lab3_hcheresal_add import camping_items as items_from_part_2lab 

camping_items: List[str] = items_from_part_2lab.copy() 

replacemiddile_index:int = len(camping_items) // 2  
camping_items[replacemiddile_index] = "binoculars" 

def main() -> None: 
    '''printing slices around 'binoculars''''
    binocular_index: int = camping_items.index("binoculars")
    
    
    '''binoculars is a bit long to type, now changing to bino'''
    before_bino: List[str] = camping_items[:binocular_index] 
    bino_item: str = camping_items[:binocular_index]
    '''basically copy above but add list str and add 1 to index''' 
    after_bino: List[str] = camping_items[:binocular_index + 1 :]

    print("Before binoculars:")
    print(before_bino)

    print ("\nBinoculars item")