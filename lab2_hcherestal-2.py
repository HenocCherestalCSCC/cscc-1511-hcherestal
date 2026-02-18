'''
Program Name: Used Car Receipt (Option 2)
Author: Henoc Cherestal
Purpose: This program calculates a used car total cost (tax, license, fees) and prints it in an itemized receipt.
Starter Code: None used.
Date: 02/10/2026
'''

def main() -> None: 
    base_price: float = 18500.00 

    tax_rate: float = 0.065 #6.5% this is the 6.5 tax 
    license_rate: float = 0.0125 #1.25% personal chosen license 

    title_fee: float = 75.00
    dealer_prep_fee: float = 299.00
    destination_fee: float = 495.00 

    tax: float = base_price * tax_rate 
    license_fee: float = base_price * license_rate 

    total: float = (
        base_price
        + tax 
        + license_fee 
        + title_fee
        + dealer_prep_fee
        + destination_fee
    )

#OUTPUT!!! 

    print("========================================") 
    print("         USED CAR PURCHASE RECEIPT      ") 
    print("========================================") 
    print(f"{'Base Price:':20}  ${base_price:10.2f}") 
    print(f"{'Tax (6.5%):':20} ${tax:10.2f}")
    print(f"{'License Fee:':20} ${license_fee:10.2f}") 
    print(f"{'Title Fee:':20} ${title_fee:10.2f}")
    print(f"{'Dealer Prep:':20} ${dealer_prep_fee:10.2f}")
    print(f"{'Destination:':20} ${destination_fee:10.2f}") 
    print("----------------------------------------")
    print(f"{'TOTAL:':20} ${total:10.2f}")
    print("========================================")

    if __name__ == "__main__": 
        main()