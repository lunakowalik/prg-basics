###
# Allows to enter and print employee data. Due to personal
# data protection, you can determine whether information about
# the employee's salary will be printed
#
from keyboard import * # your own defined module

# Reads employee's data from keyboard
first_name = input_string('Enter first name: ')
last_name = input_string('Enter last name: ')
age = input_integer("Enter age: ")
salary = input_integer("Enter salary: ")
is_salary_hidden = input_boolean('Hide salary? (y/n) ')

# Prints employee's record
print('DATA RECORD')
print('===========')
print('First Name:', first_name)
print('Last Name:', last_name)
print('Age:', age)
if not is_salary_hidden:
    print('Salary:', salary)