def hide(card_number):
    card_str = str(card_number)
    return card_str[:2] + "*" * (len(card_str) - 6) + card_str[-4:]