numbers = []
for i in range(1, 31):
    if i % 3 == 0 and i % 5 == 0:
        numbers.append("BINGO")
    elif i % 3 == 0:
        numbers.append("THREE")
    elif i % 5 == 0:
        numbers.append("FIVE")
    else:
        numbers.append(str(i))

print(" ".join(numbers))
