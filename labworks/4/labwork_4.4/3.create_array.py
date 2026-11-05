n = int(input("Enter size: "))

a = []
b = []
c = []

print("Enter A:")
for i in range(1, n + 1):
    a.append(int(input("Enter number: ")))

print("Enter B:")
for i in range(1, n + 1):
    b.append(int(input("Enter number: ")))

for i in range(1, n + 1):
    c.append(a[i - 1] + b[i - 1])

print("Array C is:", c)