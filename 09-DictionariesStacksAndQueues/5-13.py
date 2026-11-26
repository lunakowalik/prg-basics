import queue

stack = queue.LifoQueue()

while True:
    x = input()
    if x == "=":
        print(stack.get())
        break
    elif x == "+":
        b = stack.get()
        a = stack.get()
        stack.put(a + b)
    elif x == "-":
        b = stack.get()
        a = stack.get()
        stack.put(a - b)
    elif x == "*":
        b = stack.get()
        a = stack.get()
        stack.put(a * b)
    elif x == "/":
        b = stack.get()
        a = stack.get()
        stack.put(a / b)
    else:
        stack.put(float(x))