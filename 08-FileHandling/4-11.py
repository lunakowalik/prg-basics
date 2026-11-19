file_name = "powers.txt"

with open(file_name, "w", encoding="utf-8") as file:
    for n in range(1, 101):
        square = n ** 2
        cube = n ** 3
        line = f"{n},{square},{cube}"
        print(line)
        file.write(f"{line}\n")