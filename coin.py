'''
Program Name: Coin Class
Author: Henoc Cherestal
Purpose: This file creates the Coin class for the Match Coins game.
It represents ONE coin that can be tossed and can report
whether it landed on Heads or Tails.
Starter Code: None
Date: 03/23/2026
''' 

import random

class Coin:

    def __init__(self) -> None:
        '''this is to make it have a starting side'''
        self.__sideup: str = "Heads"

    def toss(self) -> None:
        '''random toss up and get heads or tails'''
        if random.randint(0, 1) == 0:
            self.__sideup = "Heads"
        else:
            self.__sideup = "Tails"

    def get_sideup(self) -> str:
        '''which side is facing up'''
        return self.__sideup