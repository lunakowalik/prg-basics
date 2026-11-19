import mod_7_5

number = int(input("A number: "))
print(f"Number {number} in the range <2,15>: ", "yes" if mod_7_5.in_range(number, 2, 15) else "no")