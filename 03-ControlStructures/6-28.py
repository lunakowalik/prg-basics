a = 1
b = 0
c = 0
for i in range(20):
    print(a, end=" ")
    c = a + b
    b = a
    a = c
