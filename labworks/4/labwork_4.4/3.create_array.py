n = int(input("Enter size: "))

a = []
b = []
c = []

print("Enter A:")
for i in range(n):
    a.append(int(input()))

print("Enter B:")
for i in range(n):
    b.append(int(input()))

for i in range(n):
    c.append(a[i] + b[i])

print("Array C is:", c)