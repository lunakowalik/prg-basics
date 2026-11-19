import re

text = input("Enter text: ")

# Matches English vowels (case-insensitive)
vowels = re.findall(r"[aeiouAEIOU]", text)

print("Number of vowels:", len(vowels))