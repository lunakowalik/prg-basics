price_list = {
   'T-shirt': 19.99,
   'Jeans': 49.99,
   'Jacket': 89.99,
   'Sneakers': 59.99,
   'Hat': 15.99
}

print("Products and prices before discount:")
for product, price in price_list.items():
    print(f"{product}: {price:.2f}")

total_before = sum(price_list.values())
print(f"Total value before discount: {total_before:.2f}")

for product in price_list:
    price_list[product] = round(price_list[product] * 0.90, 2)

print("\nProducts and prices after 10% discount:")
for product, price in price_list.items():
    print(f"  {product}: {price:.2f}")

total_after = sum(price_list.values())
print(f"Total value after discount: {total_after:.2f}")