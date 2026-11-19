import re

file_name = "files.txt"
pattern = re.compile(r"\.[^.\s]{4}$")

with open(file_name, "r", encoding="utf-8") as file:
    for line in file:
        entry = line.strip()
        if entry and pattern.search(entry):
            print(entry)