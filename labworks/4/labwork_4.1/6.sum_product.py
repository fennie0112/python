def calculate(*num):
    total = sum(num)

    product=1
    for x in num:
        product = product*x
        return total,product

print(calculate(2,3,4))
    

    