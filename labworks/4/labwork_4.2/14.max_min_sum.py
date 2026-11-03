def calculate(numbers):
    return sum(numbers), max(numbers), min(numbers)

numbers = [10, 20, 5, 30, 15]

s, maximum, minimum = calculate(numbers)

print("Sum =", s)
print("Maximum =", maximum)
print("Minimum =", minimum)