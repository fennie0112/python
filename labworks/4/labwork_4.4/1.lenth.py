n = int(input("Enter size: "))
arr = []

for i in range(n):
    arr = arr + [int(input("Enter number: "))]

count = 0
for i in arr:
    count = count + 1

print("Length:", count)