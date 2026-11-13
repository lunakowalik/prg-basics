correct_pin = "0805"
tries = 0
while True:
    pin = input("Enter the PIN code: ")
    if pin == correct_pin:
        print("Correct!")
        break
    else:
        print("Incorrect...")
        tries += 1
        if tries == 3:
            print("Sorry, your payment card has been blocked")
            break
