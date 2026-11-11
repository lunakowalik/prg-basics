###
# A program that prints a university abbreviation
#   
university = "Krakow University of Economics"

words = university.split()
capital_words = filter(lambda w: w[0].isupper(), words)
initials_of_capital_words = [w[0] for w in capital_words]
abbreviation = "".join(initials_of_capital_words)

print(abbreviation)