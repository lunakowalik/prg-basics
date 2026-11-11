###
# Calculation of circle area and circumference 
#

# determine radius and PI values
r = float(input("Enter radius: "))
pi = 3.14 # would've used a library, but this seems like what the author meant

# calculate area
area = r ** 2 * pi
# calculate circumference
circumference = r * 2 * pi
# print results
print(f"Area: {area}")
print(f"Circumference: {circumference}")