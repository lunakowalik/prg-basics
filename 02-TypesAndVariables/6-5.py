###
# a program that prints a 9-digit telephone number
# entered from the keyboard as three groups of 3 digits each,
# separated by a dash character.
#
phone = input('Enter phone number: ')

# split into groups of 3
groups = [phone[i*3:(i+1)*3] for i in range(3)]

formatted = "-".join(groups)

print(f"Phone number: {formatted}")