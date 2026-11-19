import csv

file_name = "clothing.csv"
max_price = 60.0
max_stock = 40

try:
    with open(file_name, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            price = float(row["Price"].strip())
            stock = int(row["Stock_Quantity"].strip())

            if price < max_price and stock < max_stock:
                print(
                    f"{row['Product_ID'].strip()} | {row['Product_Name'].strip()} | "
                    f"{row['Category'].strip()} | Size: {row['Size'].strip()} | "
                    f"{row['Color'].strip()} | ${price:.2f} | Stock: {stock}"
                )

except FileNotFoundError:
    print(f"Error: '{file_name}' was not found.")