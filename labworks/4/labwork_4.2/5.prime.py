a = int(input("Enter starting number: "))
b = int(input("Enter ending number: "))

for n in range(a, b + 1):
    if n < 2:
        continue

    prime = True

    for i in range(2, n):
        if n % i == 0:
            prime = False
            break

    if prime:
        print(n, end=" ")