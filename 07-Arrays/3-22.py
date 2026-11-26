arr = [7, 9, 2, 4, 5, 6]
evens = []
odds = []

for x in arr:
    if x % 2 == 0:
        evens.append(x)
    else:
        odds.append(x)

arr = evens + odds
print("arr =", arr)