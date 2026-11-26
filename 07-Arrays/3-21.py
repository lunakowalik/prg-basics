arr = [6.11, 15.2, 5.1, 3.2, 15.9, 12.5]
threshold = float(input("Enter a value: "))
count = 0

for x in arr:
    if x > threshold:
        count += 1

print("Array:", *arr)
print("Count:", count)