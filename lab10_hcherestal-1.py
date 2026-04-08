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
    #'''analyzing the wordcounts in the .txt files. '''
    def __init__(self, filepath: str) -> None: 
        #'''set up dictionary of file path'''
        self.__filepath: Path = Path(filepath)
        self.__frequencies: dict[str, int] = {}
    

    #'''reading the file and cleaning the text and counting each word'''
    def process_file(self) -> bool: 
        try:
            if not self.__filepath.exists():
                raise FileNotFoundError
            
            translation_table = str.maketrans("", "", string.punctuation)

            with self.__filepath.open("r", encoding="utf-8") as file: 
                for line in file: 
                    clean_line = line.lower().translate(translation_table)
                    words = clean_line.split()

                    for word in words: 
                        if word in self.___frequencies: 
                            self.__frequencies[word] += 1 
                        else:
                            self.__frequencies[word] = 1 

            return True 

        except FileNotFoundError
            print(f"\nError: The file '{self.__filepath.name}' was not found.")
            return False  

    def print_report(self) -> None:
            """Print the words and their counts in alphabetical order."""
            sorted_words = sorted(self.__frequencies.keys())

            print()
            for word in sorted_words:
                print(f"{word:<20}:: {self.__frequencies[word]}")    