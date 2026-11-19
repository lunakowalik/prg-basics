def sum_digits(number):
    number = abs(number)
    digits = [int(d) for d in str(number)]
    return sum(digits)

any_number = int(input('Enter integer number: '))
result = sum_digits(any_number)
print(f'The sum of the digits in the number {any_number} is {result}')
