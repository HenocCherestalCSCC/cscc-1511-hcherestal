'''
Program Name: THE BEST UPC Validator 
Author: Henoc Cherestal 
Purpose: This program asks the user to enter a 12-digit UPC code and checks if it is valid.
         It does this by calculating the expected check digit using the UPC algorithm
         and comparing it to the last digit entered by the user. 
Starter Code: None
Date: 03/09/2026
''' 

def find_UPC(first11:str) -> int: 
    '''Here I have to caluculate the correct UPC check digit from the first 11 digits'''