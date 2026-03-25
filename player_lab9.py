'''
Program Name: Player Class
Author: Henoc Cherestal
Purpose: This file creates the Player class for the Match Coins game.
         A player has a name, a wallet of coins, and a Coin object.
Starter Code: None
Date: 03/24/2026
'''

from coin_lab9 import Coin 

class Player:

    def __init__(self, name: str) -> None:
        '''initialize the name wallet and coin'''
        self.__name: str = name
        self.__wallet: int = 20
        self.__coin: Coin = Coin()