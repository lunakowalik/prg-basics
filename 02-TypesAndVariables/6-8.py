###
# A program that calculates
# how many letters are between two given letters
#
first = input('Enter first letter: ')
last = input('Enter last letter: ')
first_letter_code = ord(first)
last_letter_code = ord(last)
number_of_letters = last_letter_code - first_letter_code - 1 if first != last else 0 
# the -1 expression is needed because we're counting how many letters are between not how distant they are
# I have no idea how this could be done without control structures

print(f'Between {first} and {last} is {number_of_letters} letters')