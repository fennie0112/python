n = int(input("Enter n: "))

def series(i):
    if i == 5:
        return 0
    return 1 / n**i + series(i + 1)

print("Sum =", series(0))