with open('pets.txt') as file:
    text = file.read()

print(text)

word_count = len(text.split())
print('Number of words:', word_count)