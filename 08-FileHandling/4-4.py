file_name = 'it_company.csv'

with open(file_name, 'r', encoding='utf-8') as file:
    count = 0
    for line in file:
        print(line.rstrip('\r\n'))
        count += 1
        if count == 5:
            input('Press Enter key...')
            count = 0