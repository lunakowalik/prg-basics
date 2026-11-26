import json

product = {}

# read product data from keyboard
product["name"] = input("Name: ")
product["price"] = float(input("Price: "))
product["paid"] = input("Paid (yes/no): ").strip().lower() == "yes"

# save product data to json file
with open("product.json", "w", encoding="utf-8") as f:
    json.dump(product, f)