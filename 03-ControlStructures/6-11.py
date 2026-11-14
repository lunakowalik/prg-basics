current_price = float(input("Current product price: "))
previous_price = float(input("Previous price: "))

change = int((previous_price - current_price) / previous_price * 100)
if change >= 10:
    print("Buy the product!!")
    print(f"Product price reduced by {change}%")
