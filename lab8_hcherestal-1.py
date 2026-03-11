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

    odd_sum = 0 
    even_sum = 0 

    for i in range(len(first11)):
        digit = int(first11[i])

        if i % 2 == 0:
            odd_sum += digit 
        else: 
            even_sum += digit 

    total = (odd_sum * 3) + even_sum
    check_digit = (10 - (total % 10)) % 10 

    return check_digit

def main() -> None: 
    ''' Now i have to run the UPC validation program '''
    ''' Doesn't really need a main but its cleaner in my opinion to put the main logic in it '''
    while True: 
        upc: str = input("Enter a 12-digit UPC: ").strip()

        if len(upc) != 12 or not upc.isdigit(): 
            print("INVALID INPUT. Please enter exactly 12 digits.\n")
            continue

        break

    first11: str = upc[:11]
    provided_digit: int = int(upc[11])

    print(f"\nThe first 11 digits are '{first11}'.")
    print(f"The provided check digit is '{provided_digit}'.\n")
    print("Calculating...")

    expected_digit = find_UPC(first11)

    print(f"The expected check digit is {expected_digit}.\n")

    if expected_digit == provided_digit: 
        print("This is a VALID UPC.")
    else:
        print("This is an INVALID UPC.") 


main()

