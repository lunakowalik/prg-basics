amount = int(input("Number of products purchased: "))
price = float(input("Product price: "))

if amount > 2:
    amount_to_pay = 2 * price + (amount - 2) * price * 0.75
else:
    amount_to_pay = price * amount

print(f"Amount to pay {amount_to_pay:.2f}")
