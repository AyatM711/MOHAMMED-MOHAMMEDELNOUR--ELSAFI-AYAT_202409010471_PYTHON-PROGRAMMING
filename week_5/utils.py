# this is a function for calculating
def calculate_total(coffee, tea, sandwich):
    price_coffee = 8.50
    price_tea = 6.00
    price_sandwich = 12.00
    
    total = (coffee * price_coffee) + (tea * price_tea) + (sandwich * price_sandwich)
    return total

# this is a function for printing the receipt
def print_receipt(name, coffee, tea, sandwich, total):
    print("\n===== RECEIPT =====")
    print(f"Customer : {name}")
    print(f"Coffee   : {coffee}")
    print(f"Tea      : {tea}")
    print(f"Sandwich : {sandwich}")
    print("-------------------")
    print(f"Total = RM {total:.2f}")
