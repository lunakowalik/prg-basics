import math

h = int(input("Height: "))

# f(h) = 3.57 * sqrt(h)  [in km]
d = 3.57 * math.sqrt(h)

print("Distance to horizon: ", d, "km")