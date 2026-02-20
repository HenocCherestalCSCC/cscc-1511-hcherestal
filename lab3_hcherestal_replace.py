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

