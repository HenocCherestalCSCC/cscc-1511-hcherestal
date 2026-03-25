'''
Program Name: Match Coins Game
Author: Henoc Cherestal
Purpose: This program runs a two-player Match Coins game using
         the Player and Coin classes. Players toss coins and gain
         or lose coins depending on whether the tosses match.
Starter Code: None
Date: 03/24/2026
'''

from player import Player


def main() -> None:
    """Run the Match Coins game."""
    player1 = Player("Player 1")
    player2 = Player("Player 2")

    print("--- Coin Match Game ---")
    print(f"{player1.get_name()} has {player1.get_wallet()} coins.")
    print(f"{player2.get_name()} has {player2.get_wallet()} coins.")

    play_again = input("\nDo you want to toss the coins? (y/n): ")

    while play_again.lower() == "y":
        print("\nTossing...")

        player1.toss_coin()
        player2.toss_coin()

        side1 = player1.get_coin_side()
        side2 = player2.get_coin_side()

        print(f"{player1.get_name()} tossed {side1}")
        print(f"{player2.get_name()} tossed {side2}")