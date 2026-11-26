t = (10, 20, 30, 40, 50)
rev = []

print("Tuple:", ",".join(str(x) for x in t))

print("Reverse order: ", end="")
for i in range(len(t) - 1, -1, -1):
    print(str(t[i])+("," if i != 0 else ""), end="")

print()