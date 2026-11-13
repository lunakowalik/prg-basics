amount = int(input("Enter the amount in PLN: "))

print(f"The amount of PLN {amount} in coins")

coins5 = amount // 5
amount -= coins5 * 5

coins2 = amount // 2
amount -= coins2 * 2

coins1 = amount

print(f"5 PLN coins: {coins5}")
print(f"2 PLN coins: {coins2}")
print(f"1 PLN coins: {coins1}")
