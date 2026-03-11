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

# NOTE: I tested the 'invalid' output example but it is actually valid when it comes to the standard UPC-A Checksum algorithm? 
# 074590508994 is actually VALID, is this a trick question? 

# First 11 digits: 07459050899
#
# Odd positions (1,3,5,7,9,11):
# 0 + 4 + 9 + 5 + 8 + 9 = 35
#
# Multiply by 3:
# 35 * 3 = 105
#
# Even positions (2,4,6,8,10):
# 7 + 5 + 0 + 0 + 9 = 21
#
# Add totals:
# 105 + 21 = 126
#
# Find check digit:
# 126 % 10 = 6
# 10 - 6 = 4
#
# The expected check digit is 4, which matches the provided digit?
# 

main()

