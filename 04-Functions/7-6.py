import mod_7_6

cards = [
    "5290312400019022",
    "4532891044551234",
    "5105105105105100",
]

for card in cards:
    hidden = mod_7_6.hide(card)
    print(f'f("{card}") returns "{hidden}"')