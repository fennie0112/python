n = int(input("Enter size: "))
arr = []

for i in range(1,n+1):
    arr = arr + [int(input("Enter number: "))]
print("Array:", arr)

count = 0
for i in arr:
    count = count + 1

print("Length:", count)