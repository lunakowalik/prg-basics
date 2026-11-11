###
# A program that prints your height both in cm and in feet and inches.
#
import math

cm = 170
feet = math.floor(cm / 30.48)
inches = round((cm - (feet * 30.48)) * 0.39)
# calculate the number of feet

print(f'I am {cm}cm tall, i.e. {feet} feet and {inches} inches')