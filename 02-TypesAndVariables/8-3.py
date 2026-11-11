###
# A program that reads temperature in degrees Celsius from the keyboard.
# Use comments to briefly describe the program's algorithm.
#

celsius = int(input("Celsius: "))

# calculate fahrenheit
fahrenheit = celsius * 9 // 5 + 32

# calculate kelvin
kelvin = celsius + 273

# print results
print(f"Fahrenheit: {fahrenheit}")
print(f"Kelvin: {kelvin}")