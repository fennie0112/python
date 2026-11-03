def factorial(n):
    if (n < 0):
        return "Factorial not possible"

    elif (n == 0 or n == 1):
        return 1

    else:
        result = n
        n -= 1
        return result * factorial(n)


num = int(input("Input a number: "))
print("Factorial:", factorial(num))