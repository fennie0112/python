num = 0

def initialize():
    global num
    num = 10

def increment():
    global num
    num = num + 1

initialize()
increment()

print("Number =", num)