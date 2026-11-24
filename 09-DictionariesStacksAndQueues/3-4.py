import queue

number = int(input("Natural number: "))
stack = queue.LifoQueue()

if number == 0:
    stack.put(0)
else:
    current = number
    while current > 0:
        stack.put(current % 2)
        current //= 2

bits = []
while not stack.empty():
    bits.append(str(stack.get()))

print("Binary number:", "".join(bits))