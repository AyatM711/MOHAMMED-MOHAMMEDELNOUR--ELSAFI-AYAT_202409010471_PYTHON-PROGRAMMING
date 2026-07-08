from food_order import calculate_total

def main():
    price = float(input("Price(RM): "))
    quantity = int(input("Quantity: "))
    
    total = calculate_total(price, quantity)
    
    # Check if we got an error text or a valid float number
    if isinstance(total, str):
        print(f"Error: {total}")
    else:
        print(f"Total Payment = RM {total:.2f}")

if __name__ == "__main__":
    main()