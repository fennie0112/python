n = int(input("Enter size: "))
arr = []

for i in range(n):
    arr.append(int(input("Enter number: ")))

print("\n\nEven numbers:")
for x in arr:
    if x % 2 == 0:
        print(x)

print("\n\nOdd numbers:")
for x in arr:
    if x % 2 != 0:
        print(x)