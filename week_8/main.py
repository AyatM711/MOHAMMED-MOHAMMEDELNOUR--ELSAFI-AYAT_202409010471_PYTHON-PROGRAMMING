# Import functions from our custom modules
from customer import get_customer
from receipt import print_receipt

def main():
    # Gather data using the customer module
    name, food, quantity, price, delivery_charges = get_customer()
    
    # Pass the data to the receipt module to print it out
    print_receipt(name, food, quantity, price, delivery_charges)

if __name__ == "__main__":
    main()
