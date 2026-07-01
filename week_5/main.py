from utils import calculate_total, print_receipt

def main():
    # Prompting for user inputs matching the sample input format
    name = input("Customer name: ")
    coffee_qty = int(input("Coffee quantity: "))
    tea_qty = int(input("Tea quantity: "))
    sandwich_qty = int(input("Sandwich quantity: "))
    
    # Calculate the grand total bill amount
    grand_total = calculate_total(coffee_qty, tea_qty, sandwich_qty)
    
    # Display the structured receipt output
    print_receipt(name, coffee_qty, tea_qty, sandwich_qty, grand_total)

if __name__ == "__main__":
    main()
