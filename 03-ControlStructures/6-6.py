hours = int(input('Enter number of hours parked: '))

if hours < 2:
    fee = 5
elif hours < 6:
    fee = 15
else:
    fee = 20

print(f"Parking fee is equal to {fee}")