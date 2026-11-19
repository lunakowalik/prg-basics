###
# Calculates the total value of money spent
#
import re  # module for regular expressions

# file name with shopping report
email_file = 'report.txt'

# read the content of email
with open(email_file, 'r', encoding='utf-8') as file:
   email = file.read()

# regular expression pattern
# for amounts (matches integers or decimals like 12, 19.99, or 19,99)
pattern = r'\d+(?:[.,]\d+)?'

# extract numbers from email
# tip: findall() method returns an array
amounts = re.findall(pattern, email)

# calculate the total purchases
total = 0.0
for amount in amounts:
   total += float(amount.replace(',', '.'))

# print result
print(f"Total spent: {total:.2f}")