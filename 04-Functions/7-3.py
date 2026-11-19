def month_name(month):
    if month < 1 or month > 12:
        return ''
    name = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"][month - 1]
    return name

month_number = int(input("Enter month number: "))
print(f"The name of month {month_number} is {month_name(month_number)}")