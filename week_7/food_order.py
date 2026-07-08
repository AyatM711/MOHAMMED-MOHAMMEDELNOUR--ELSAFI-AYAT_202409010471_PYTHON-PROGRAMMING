
def calculate_total(price, quantity):
    # Blank completed: validation checks matching test requirements
    if price <= 0:
        return "invalid price"
    if quantity <= 0:
        return "invalid quantity"
        
    return price * quantity