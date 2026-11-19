###
# Functions to read any data type from the keyboard
#
def input_string(message):
    s = input(message)
    return s

def input_integer(message):
    s = input(message)
    return int(s)

def input_real(message):
    s = input(message)
    return float(s)

def input_boolean(message):
    s = input(message)
    return s == 'y'
