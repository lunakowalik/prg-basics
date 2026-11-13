number = int(input("Enter number: "))

remainders = []
acc = number
while acc > 0:
    rem = acc % 2
    remainders.append(str(rem))
    acc //= 2

# remainders need to be reversed to give us the digits of the number
digits = remainders[::-1]
binary = "".join(digits)
print(f"{number}(10) = {binary}(2)")
