arr = [10,20,30,40,50]
num = int(input("Enter number: "))
if num in arr:
    print(arr.index(num))
else:
    print("Not Found")