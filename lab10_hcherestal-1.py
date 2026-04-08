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
                        if word in self.__frequencies: 
                            self.__frequencies[word] += 1 
                        else:
                            self.__frequencies[word] = 1 

            return True 

        except FileNotFoundError:
            print(f"\nError: The file '{self.__filepath.name}' was not found.")
            return False  

    def print_report(self) -> None:
            #'''Print the words and their counts in abc order.'''
            sorted_words = sorted(self.__frequencies.keys())

            print()
            for word in sorted_words:
                print(f"{word:<20}:: {self.__frequencies[word]}")     

def main() -> None:
    # '''this is to run the actual program.'''
    base_path = Path(__file__).parent

    files = {
        "1": base_path / "monte_cristo.txt",
        "2": base_path / "treasure_island.txt",
        "3": base_path / "tarzan.txt",
        "4": base_path / "princess_mars.txt",
    }

    while True:
        print("\n--- Word Analyzer ---")
        print("Please select a file to analyze:")
        print("1. Monte Cristo")
        print("2. Treasure Island")
        print("3. Tarzan")
        print("4. Princess of Mars")
        print("5. Exit")

        choice = input("\nEnter your choice (1-5): ").strip()

        if choice == "5":
            print("\nGoodbye!")
            break 

        if choice not in files:
            print("\nInvalid choice. Please select from 1-5.")
            input("\nPress Enter to return to the menu...")
            continue 

        selected_path = files[choice]
        analyzer = WordAnalyzer(str(selected_path))

        print(f"\nProcessing '{selected_path.name}'...")

        if analyzer.process_file():
            analyzer.print_report()