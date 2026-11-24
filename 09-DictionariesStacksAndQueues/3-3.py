import queue

stack = queue.LifoQueue()

def brackets_ok(expression):

    for c in expression:
        if c in ['{', '[', '(']:
            stack.put(c)
        if c in ['}', ']', ')']:
            opened = stack.get()
            if c == '}' and opened != '{':
                return False
            if c == ']' and opened != '[':
                return False
            if c == ')' and opened != '(':
                return False
    return stack.empty()

expression1 = "[(2+3)*4+5]/6-{(7*8)+[4]}" # brackets ok
expression2 = "[(2+3]/4)"                 # brackets not correct
expression3 = "(2-3*4+(5/6)"              # brackets not correct

if brackets_ok(expression1):
    print("Expression 1's use of brackets is correct")
else:
    print("Expression 1's use of brackets is incorrect")

if brackets_ok(expression2):
    print("Expression 2's use of brackets is correct")
else:
    print("Expression 2's use of brackets is incorrect")

if brackets_ok(expression3):
    print("Expression 3's use of brackets is correct")
else:
    print("Expression 3's use of brackets is incorrect")