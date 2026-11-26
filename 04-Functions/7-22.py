def f(name):
    return "".join([word[0] for word in name.split()])


print(f'f("Internet of Things") returns "{f("Internet of Things")}"')
print(f'f("For Your Information") returns "{f("For Your Information")}"')
print(f'f("Python") returns "{f("Python")}"')