import queue

text = input("Enter text to reverse: ")

stack = queue.LifoQueue()

for char in text:
    stack.put(char)

reversed_chars = []
while not stack.empty():
    reversed_chars.append(stack.get())

print("Reversed text:", "".join(reversed_chars))