N = int(input("Enter N: "))

next = 2
for i in range(N):
    while True:
        is_prime = True
        for j in range(2, next):
            if next % j == 0:
                is_prime = False
                break
        next += 1
        if is_prime:
            print(next - 1, end=" ")
            break
