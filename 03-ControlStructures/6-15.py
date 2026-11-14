ean13 = input("Enter EAN-13 article number: ")
if len(ean13) != 13 or not ean13.isdigit():
    print("Article number is not correct")
else:
    print("Article number is correct")
    if ean13[0:3] == "590":
        print("Article manufactured in Poland")
