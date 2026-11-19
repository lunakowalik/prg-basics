import queue

"""
A stack is a linear data structure that follows
the Last In, First Out (LIFO) principle.
This means the last element added to the stack
is the first one to be removed. Think of a stack
as a pile of plates — the last plate you place
on the top is the first one you'll take off.
"""

# creates a stack
numbers = queue.LifoQueue()

numbers.put(2)
numbers.put(3)
numbers.put(7)
numbers.put(4)
numbers.put(1)
numbers.put(9)
numbers.put(8)

print("Sum of two last numbers:", numbers.get() + numbers.get())

s = 0
while True:
    try:
        n = numbers.get(False)
    except queue.Empty:
        break
    s += n

print("Sum of rest:", s)