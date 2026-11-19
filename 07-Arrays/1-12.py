categories = ["Food", "Transport", "Rent","Entertainment"]
expenses = [500, 150, 1000, 200]

max_exp = 0
for i in range(len(expenses)):
    if expenses[i] > expenses[max_exp]:
        max_exp = i

print("Most expensive category:", categories[max_exp], expenses[max_exp])