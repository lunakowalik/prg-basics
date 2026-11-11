###
# String manipulation
#

movie = "The Lord of the Rings: The Return of the King"

# print number of characters
print('Number of characters: ', len(movie))

# print title in capital letters
print('Title in capital letters: ', movie.upper())

# print title in small letters
print("Title in small letters: ", movie.lower())

# print how many times the vowel "e" appears in the title
print("Vowel e appears ", movie.lower().count('e'), "times in the title")

# print where in the text is the word "Lord"
print("The word 'Lord' appears after character number ", movie.find('Lord'))

# print where in the text is the word "dragon"
print("The word 'dragon' appears after character number ", movie.find('dragon'))
# It doesn't appear, but I think this is what the author meant ???