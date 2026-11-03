def digit_sum(n):
    if n < 10:
        return n

    last = n % 10
    remaining = n // 10
    return last + digit_sum(remaining)

n = int(input("Enter a number: "))
print("Sum =", digit_sum(n))