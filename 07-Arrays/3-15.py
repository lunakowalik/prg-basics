def occurs(number, array):
    for x in array:
        if x == number:
            return True
    return False


arr = [15, 38, 7, 23, 14]
num = int(input("Number: "))

print("Number:", num)
print("Array:", *arr)
if occurs(num, arr):
    print(f"Result: number {num} appears in the array")
else:
    print(f"Result: number {num} does not appear in the array")