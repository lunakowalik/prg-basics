number = int(input("Enter number: "))

remainders = []
while number > 0:
    rem = number % 2
    remainders.append(str(rem))
    number //= 2

# remainders need to be reversed to give us the digits of the number
digits = remainders[::-1]
print("Number in binary:", "".join(digits))
