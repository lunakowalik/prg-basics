###
# Prints some array elements
#
arr = [2, 3, 7, 5, 4]

print(arr)
print('Number of elements', len(arr))
print('First value', arr[0])
print('Second value', arr[1])
print('Second value', arr[-1])
print('Second value', arr[len(arr)-2])
print('Sum of first and last value', arr[0] + arr[-1])
print('Middle value', arr[len(arr)//2])

print("all array values seperated by a single space ", end="")
for v in arr:
    print(v, end=" ")