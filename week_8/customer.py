def get_customer():
    print("=== Customer Information ===")
    
    # 1. Gather inputs from the user
    name = input("Customer Name: ")
    food = input("Food Ordered (Cake/Muffin): ")
    quantity = int(input("Quantity: "))
    price = float(input("Price per Item (RM): "))
    delivery_option = input("Delivery (Y/N): ").strip().upper()
    
    # 2. Logic to determine delivery charges
    if delivery_option == "Y":
        delivery_charges = 5.00
    else:
        delivery_charges = 0.00
        
    return name, food, quantity, price, delivery_charges
