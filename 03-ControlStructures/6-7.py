age = int(input('Enter age: '))

if age < 13:
    age_group = "a child"
elif age < 19:
    age_group = "a teen"
elif age < 64:
    age_group = "an adult"
else:
    age_group = "a senior"

print(f"The user is {age_group}.")
