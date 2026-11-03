total = 0

def add(n):
    global total
    total = total + n

for i in range(3):
    n = int(input("Enter number: "))
    add(n)

print("Sum =", total)