names = ["Genowefa", "Onufry", "Celestyna", "Alojzy", "Pankracy"]
longest = names[0]

for name in names[1:]:
    if len(name) > len(longest):
        longest = name

print("Names:", *names)
print("Longest name:", longest)