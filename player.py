'''
Program Name: Player Class
Author: Henoc Cherestal
Purpose: This file creates the Player class for the Match Coins game.
         A player has a name, a wallet of coins, and a Coin object.
Starter Code: None
Date: 03/24/2026
'''

from coin import Coin 

class Player:

    def __init__(self, name: str) -> None:
        '''initialize the name wallet and coin'''
        self.__name: str = name
        self.__wallet: int = 20
        self.__coin: Coin = Coin() 

    def toss_coin(self) -> None:
        '''toss the coin'''
        self.__coin.toss()

    def get_coin_side(self) -> str:
        '''which side of coin?'''
        return self.__coin.get_sideup()

    def win_coin(self) -> None:
        '''adding coin to wallet'''
        self.__wallet += 1

    def lose_coin(self) -> None:
        '''-1 coin from wallet'''
        self.__wallet -= 1

    def get_wallet(self) -> int:
        '''return how many coins are left in wallet'''
        return self.__wallet

    def get_name(self) -> str:
        '''return the players name'''
        return self.__name    