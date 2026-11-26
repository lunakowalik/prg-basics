import json

with open("euro.json", "r", encoding="utf-8") as f:
    data = json.load(f)

print("Date            Buying Rate     Selling Rate")
print("============================================")
for r in data["rates"]:
    print(f"{r['effectiveDate']:<16}{r['bid']:<16.4f}{r['ask']:.4f}")