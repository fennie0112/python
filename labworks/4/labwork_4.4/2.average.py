n = int(input("Enter size: "))
s = 0

for i in range(1,n+1):
    x = int(input("Enter number: "))
    s = s + x

print("Average:", s / n)