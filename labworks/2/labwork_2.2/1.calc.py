num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
op = input("Enter an operator (+, -, *, /): ")

match op:
    case '+':
        print("Result:", num1 + num2)
    case '-':
        print("Result:", num1 - num2)
    case '*':
        print("Result:", num1 * num2)
    case '/':
        if num2 != 0:
            print("Result:", num1 / num2)
        else:
            print("!!!!......Error......!!!")
    case _:
        print("Invalid operator")