from food_order import calculate_total

def main():
    price=float(input("Price(RM):"))
    quantity=int(input("Quantity:"))
    
    # Blank completed: calls the imported function with inputs
    total = calculate_total(price, quantity)
    
    print(f"Total Payment = RM {total:.2f}")

# Blank completed: reconstructed the standard Python entry block
if __name__ == "__main__":
    main()