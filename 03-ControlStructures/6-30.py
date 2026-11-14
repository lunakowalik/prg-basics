W = 7
H = 7

for i in range(H):
    for j in range(1, W + 1):
        print(j + i * W, end=" ")
    print()
