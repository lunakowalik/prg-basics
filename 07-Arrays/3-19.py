t = (50, 20, 40, 50, 30, 50)
print("Tuple:", ",".join(str(x) for x in t))
val = int(input("Value: "))
count = 0

for x in t:
    if x == val:
        count += 1

print("Number of occurrences:", count)