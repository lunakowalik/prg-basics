arr = [-15, 8, -31, 47, -2, 19]
mn = arr[0]
mx = arr[0]

for x in arr[1:]:
    if x < mn:
        mn = x
    if x > mx:
        mx = x

print("Min:", mn)
print("Max:", mx)