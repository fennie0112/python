n = int(input("Enter a number: "))

def calculate(n):
    
    return n ** 2, n ** 3

result = calculate(n)

print("Square =", result[0])
print("Cube =", result[1])