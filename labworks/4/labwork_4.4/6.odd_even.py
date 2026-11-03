n = int(input("Enter size: "))
arr = []

for i in range(n):
    arr.append(int(input("Enter number: ")))

print("Even numbers:")
for x in arr:
    if x % 2 == 0:
        print(x)

print("Odd numbers:")
for x in arr:
    if x % 2 != 0:
        print(x)