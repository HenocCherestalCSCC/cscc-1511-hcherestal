'''
Program Name: Word Count Analyzer
Author: Henoc Cherestal
Purpose: This program lets the user choose from 4 text files and then
         analyzes the selected file by counting how many times each word
         appears. The results are printed in alphabetical order after then.
Starter Code: None
Date: 04/07/2026
'''

from pathlib import Path 
import string 

class WordAnalyzer:
    #analyzing the wordcounts in the .txt files. 
    def __init__(self, filepath: str) -> None: 
        #'''set up dictionary of file path'''
        self.__filepath: Path = Path(filepath)
        self.__frequencies: dict[str, int] = {}
        