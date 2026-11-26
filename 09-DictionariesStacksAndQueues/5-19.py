import json


with open("reservations.json", "r", encoding="utf-8") as f:
    res = json.load(f)["reservations"]

paid_n = sum(1 for r in res if r["paid"])
unpaid_n = len(res) - paid_n
paid_val = sum(r["nights"] * r["price_per_night"] for r in res if r["paid"])
unpaid_val = sum(r["nights"] * r["price_per_night"] for r in res if not r["paid"])
print("Number of rooms:", len(res))
print("Number of paid reservations:", paid_n)
print("Number of unpaid reservations:", unpaid_n)
print("Total value of paid reservations:", paid_val)
print("Total value of unpaid reservations:", unpaid_val)
