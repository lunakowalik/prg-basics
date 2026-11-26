import MyArrays

nums = [7, 3, 8, 5, 2]
mm = MyArrays.min_max(nums)

print("Numbers:", ",".join(str(x) for x in nums))
print("Second largest number:", MyArrays.second_largest(nums))
print("Median:", MyArrays.median(nums))
print("Smallest and largest number:", f"{mm[0]},{mm[1]}")
print("Numbers as a string:", MyArrays.to_kebab_case(nums))